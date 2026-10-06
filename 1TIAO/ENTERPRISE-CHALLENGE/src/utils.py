"""Schema e apresentação compartilhados. Nenhuma chamada externa."""
import math
from decimal import Decimal, ROUND_HALF_UP
import unicodedata
import re
import html

KEYS = ['periodo', 'empresa_id', 'veiculo_id']
COSTS = ['custo_combustivel', 'custo_pedagio', 'custo_manutencao',
         'custo_multas', 'custo_impostos', 'custo_seguro', 'outros_custos']
NUMERIC = ['km_rodados', 'litros_combustivel'] + COSTS + ['custo_total']
FIELDS = KEYS + ['tipo_veiculo'] + NUMERIC
QUALITY = ['tipo_veiculo', 'km_rodados', 'litros_combustivel'] + COSTS
LABELS = dict(zip(COSTS, ['Combustível', 'Pedágio', 'Manutenção', 'Multas',
                          'Impostos', 'Seguro', 'Outros custos']))
BENCH_NOTICE = ('Os benchmarks utilizados nesta Sprint são simulados e possuem finalidade '
                'exclusivamente acadêmica e demonstrativa. Em ambiente produtivo deverão '
                'ser substituídos por referências validadas.')

def normalize(value):
    text = unicodedata.normalize('NFKD', str(value).strip().lower())
    text = ''.join(c for c in text if not unicodedata.combining(c))
    return re.sub(r'\s+', '_', text)

def number(value, decimals=2):
    if value is None or not math.isfinite(float(value)):
        return 'Indisponível'
    rounded = Decimal(str(value)).quantize(Decimal(1).scaleb(-decimals), rounding=ROUND_HALF_UP)
    return f'{rounded:,.{decimals}f}'.replace(',', 'X').replace('.', ',').replace('X', '.')

def money(value):
    return 'Indisponível' if value is None else f'R$ {number(value)}'

def safe_text(value):
    return html.escape(str(value)).replace('|', '\\|').replace('\n', ' ').replace('\r', ' ')
