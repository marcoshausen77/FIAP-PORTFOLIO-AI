"""Indicadores de uma empresa, preservando a cobertura de cada medida."""
import pandas as pd
from utils import COSTS, LABELS
from validation import completeness

def complete_sum(series):
    return float(series.sum()) if len(series) and series.notna().all() else None

def ratio(a, b, scale=1):
    return a / b * scale if a is not None and b is not None and b > 0 else None

def analyze(df):
    if df.empty or df['empresa_id'].nunique() != 1:
        raise ValueError('Selecione uma empresa e pelo menos uma linha válida.')
    total = complete_sum(df['custo_total'])
    km = complete_sum(df['km_rodados'])
    vehicles = int(df['veiculo_id'].nunique())
    # Quando o total de uma linha é desconhecido, manter apenas suas categorias conhecidas.
    known_by_row = df['custo_total'].fillna(df[COSTS].sum(axis=1, min_count=1))
    known = float(known_by_row.sum())
    category_rows = []
    values = {}
    for c in COSTS:
        values[c] = complete_sum(df[c])
        subtotal = float(df[c].sum()) if df[c].notna().any() else None
        category_rows.append({'categoria': LABELS[c], 'campo': c,
            'valor_integral': values[c], 'subtotal_conhecido': subtotal,
            'cobertura_pct': float(df[c].notna().mean()*100),
            'participacao_pct': ratio(values[c], total, 100)})
    metrics = {
        'custo_total': total, 'subtotal_conhecido': known, 'veiculos': vehicles,
        'custo_por_veiculo': ratio(total, vehicles), 'km_total': km,
        'custo_por_km': ratio(total, km), 'custo_combustivel': values['custo_combustivel'],
        'combustivel_por_km': ratio(values['custo_combustivel'], km),
        'litros_por_100km': ratio(complete_sum(df['litros_combustivel']), km, 100),
        'manutencao_por_veiculo': ratio(values['custo_manutencao'], vehicles),
        'pedagio_por_km': ratio(values['custo_pedagio'], km),
        'multas_por_veiculo': ratio(values['custo_multas'], vehicles)}
    monthly=[]
    for period,g in df.groupby('periodo', sort=True):
        mt=complete_sum(g['custo_total']);mk=complete_sum(g['km_rodados'])
        monthly.append({'periodo':period,'custo_total':mt,'custo_por_km':ratio(mt,mk),
                        'veiculos':int(g['veiculo_id'].nunique())})
    return {'metrics': metrics, 'categories':pd.DataFrame(category_rows).sort_values(
            'subtotal_conhecido',ascending=False,na_position='last'),
            'monthly':pd.DataFrame(monthly),'quality':completeness(df)}
