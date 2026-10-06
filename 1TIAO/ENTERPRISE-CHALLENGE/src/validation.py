"""Validação bloqueante de inconsistências; lacunas opcionais são preservadas."""
from dataclasses import dataclass
import re
import numpy as np
import pandas as pd
from utils import KEYS, COSTS, NUMERIC, FIELDS, QUALITY, normalize

@dataclass
class ValidationResult:
    data: pd.DataFrame
    errors: list[str]
    warnings: list[str]
    received: list[str]

def completeness(df):
    missing = {c: int(df[c].isna().sum()) for c in QUALITY if df[c].isna().any()}
    pct = 100 * df[QUALITY].notna().to_numpy().mean() if len(df) else 0.0
    level = 'ALTA' if pct >= 90 else 'MÉDIA' if pct >= 60 else 'BAIXA'
    return {'percent': float(pct), 'level': level, 'missing': missing}

def validate(raw: pd.DataFrame) -> ValidationResult:
    df = raw.copy().reset_index(drop=True)
    df.columns = [normalize(c) for c in df.columns]
    received = list(df.columns)
    errors, warnings = [], []
    if df.empty:
        return ValidationResult(df, ['Nenhuma linha de dados.'], [], received)
    if df.columns.duplicated().any():
        return ValidationResult(df, ['Cabeçalhos duplicados após normalização.'], [], received)
    missing_keys = [c for c in KEYS if c not in df]
    if missing_keys:
        return ValidationResult(df, ['Campos obrigatórios ausentes: '+', '.join(missing_keys)], [], received)
    extra = [c for c in df if c not in FIELDS]
    if extra:
        warnings.append('Colunas ignoradas: '+', '.join(extra))
    for c in FIELDS:
        if c not in df:
            df[c] = np.nan
            warnings.append('Campo não recebido: '+c)
    df = df[FIELDS].copy()
    for c in KEYS + ['tipo_veiculo']:
        df[c] = df[c].astype('string').str.strip().replace('', pd.NA)
    for c in KEYS:
        if df[c].isna().any():
            errors.append(f'{c}: identificador/período vazio.')
    valid_period = df['periodo'].str.fullmatch(r'\d{4}-(0[1-9]|1[0-2])', na=False)
    if not valid_period.all():
        errors.append('periodo deve usar AAAA-MM, com mês válido.')
    df['tipo_veiculo'] = df['tipo_veiculo'].map(lambda x: normalize(x) if pd.notna(x) else pd.NA)
    if df.duplicated(KEYS).any():
        errors.append('Chave duplicada (empresa_id, veiculo_id, periodo). Corrija antes de analisar.')
    if (df.groupby(['empresa_id','veiculo_id'])['tipo_veiculo'].nunique() > 1).any():
        errors.append('Um mesmo veículo apresenta tipos conflitantes no arquivo.')
    for c in NUMERIC:
        strings = df[c].astype('string').str.strip().replace('', pd.NA)
        syntax_ok = strings.str.fullmatch(r'[+-]?\d+(?:[.,]\d+)?', na=True)
        converted = pd.to_numeric(strings.str.replace(',', '.', regex=False), errors='coerce').astype(float)
        invalid = strings.notna() & (~syntax_ok | ~np.isfinite(converted) | (converted < 0))
        if invalid.any():
            lines = ', '.join(str(i+2) for i in df.index[invalid][:8])
            errors.append(f'{c}: valor inválido/negativo nas linhas {lines}; use decimal sem separador de milhar.')
        df[c] = converted
    known = df[COSTS].sum(axis=1, min_count=1)
    full = df[COSTS].notna().all(axis=1)
    supplied = df['custo_total'].notna()
    mismatch = supplied & full & ((df['custo_total'] - known).abs() > .0100001)
    below = supplied & ~full & known.notna() & (df['custo_total'] < known - .0100001)
    if mismatch.any() or below.any():
        errors.append('custo_total incompatível com as categorias conhecidas (tolerância R$ 0,01).')
    if (~supplied & df[COSTS].isna().all(axis=1)).any():
        errors.append('Cada linha precisa de ao menos um custo conhecido ou custo_total.')
    df.loc[full, 'custo_total'] = known[full]
    if (df['km_rodados'] == 0).any():
        warnings.append('Há veículo-mês com km zero: não terá comparação individual por km.')
    q = completeness(df)
    if q['missing']:
        warnings.append('Dados incompletos: indicadores dependentes serão limitados; vazio não significa zero.')
    return ValidationResult(df, errors, warnings, received)
