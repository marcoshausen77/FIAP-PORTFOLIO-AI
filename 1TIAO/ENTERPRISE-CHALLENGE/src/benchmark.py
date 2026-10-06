"""Referência acadêmica local e cenários matemáticos; nenhuma inferência por LLM."""
import math
import numpy as np
import pandas as pd

CATEGORIES = ['custo_combustivel', 'custo_manutencao']
COLUMNS=['tipo_veiculo','categoria','custo_observado','km_elegiveis','taxa_observada',
         'referencia_r_por_km','desvio_r_por_km','excesso_teorico','economia_estimada',
         'linhas_elegiveis','cobertura_pct','fator_realizacao','origem','versao']

def validate_reference(ref):
    required=['tipo_veiculo','categoria','referencia_r_por_km','origem','versao']
    if any(c not in ref for c in required) or ref.empty:
        raise ValueError('Benchmark sem schema obrigatório ou vazio.')
    if ref[required].isna().any().any() or ref.duplicated(['tipo_veiculo','categoria']).any():
        raise ValueError('Benchmark contém lacunas ou referências duplicadas.')
    rates=pd.to_numeric(ref['referencia_r_por_km'],errors='coerce')
    if not (np.isfinite(rates) & (rates>0)).all():
        raise ValueError('Referências devem ser numéricas, finitas e positivas.')
    if not ref['categoria'].isin(CATEGORIES).all() or not ref['origem'].eq('SIMULADO_ACADEMICO').all():
        raise ValueError('MVP aceita apenas categorias e origem do benchmark simulado.')

def compare(df, ref, factor=.5):
    validate_reference(ref)
    if not math.isfinite(factor) or not 0<=factor<=1:
        raise ValueError('Fator de realização deve estar entre 0 e 1.')
    out=[]; coverage={}
    for cat in CATEGORIES:
        valid=(df[cat].notna() & df['km_rodados'].notna() & (df['km_rodados']>0))
        known_types=ref.loc[ref['categoria']==cat,'tipo_veiculo']
        valid &= df['tipo_veiculo'].isin(known_types)
        coverage[cat]=float(valid.mean()*100) if len(df) else 0.0
        for typ,g in df.loc[valid].groupby('tipo_veiculo'):
            r=ref.loc[(ref['categoria']==cat)&(ref['tipo_veiculo']==typ)].iloc[0]
            km=float(g['km_rodados'].sum()); cost=float(g[cat].sum());rate=float(r['referencia_r_por_km'])
            excess=max(0.0,cost-rate*km)
            out.append({'tipo_veiculo':typ,'categoria':cat,'custo_observado':cost,
                'km_elegiveis':km,'taxa_observada':cost/km,'referencia_r_por_km':rate,
                'desvio_r_por_km':cost/km-rate,'excesso_teorico':excess,
                'economia_estimada':excess*factor,'linhas_elegiveis':len(g),
                'cobertura_pct':coverage[cat],'fator_realizacao':factor,
                'origem':r['origem'],'versao':str(r['versao'])})
    table=pd.DataFrame(out,columns=COLUMNS)
    return {'table':table,'coverage':coverage,
            'economy':float(table['economia_estimada'].sum()) if len(table) else None,
            'excess':float(table['excesso_teorico'].sum()) if len(table) else None,
            'factor':factor}
