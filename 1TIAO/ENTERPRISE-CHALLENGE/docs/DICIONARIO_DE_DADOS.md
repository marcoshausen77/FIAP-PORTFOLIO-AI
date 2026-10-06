# Dicionário de dados

Granularidade: uma linha por empresa, veículo e mês. Chave composta única. Pelo menos um custo conhecido (categoria ou total) por linha. Todas as colunas constam do dataset completo, mas o MVP aceita lacunas opcionais.

| Nome | Tipo | Descrição | Unidade | Obrigatória | Utilização |
|---|---|---|---|---|---|
| periodo | texto AAAA-MM | Mês de competência | mês | Sim | Filtro, chave e série |
| empresa_id | texto | Identificador fictício da empresa | identificador | Sim | Chave e seleção da empresa |
| veiculo_id | texto | Identificador estável, sem placa | identificador | Sim | Chave e contagem |
| tipo_veiculo | texto | leve, van, caminhao ou outro tipo sem referência | categoria | Opcional | Segmentação de benchmark |
| km_rodados | decimal ≥ 0 | Distância no mês | km | Opcional | Denominador e exposição |
| litros_combustivel | decimal ≥ 0 | Volume consumido no período | L | Opcional | Consumo físico |
| custo_combustivel | decimal ≥ 0 | Despesa com combustível | BRL | Opcional individualmente | Total, ranking e indicadores da categoria |
| custo_pedagio | decimal ≥ 0 | Despesa com pedágio | BRL | Opcional individualmente | Total, ranking e indicadores da categoria |
| custo_manutencao | decimal ≥ 0 | Manutenção preventiva e corretiva | BRL | Opcional individualmente | Total, ranking e indicadores da categoria |
| custo_multas | decimal ≥ 0 | Multas registradas | BRL | Opcional individualmente | Total, ranking e indicadores da categoria |
| custo_impostos | decimal ≥ 0 | Impostos apropriados no mês | BRL | Opcional individualmente | Total, ranking e indicadores da categoria |
| custo_seguro | decimal ≥ 0 | Seguro apropriado no mês | BRL | Opcional individualmente | Total, ranking e indicadores da categoria |
| outros_custos | decimal ≥ 0 | Demais despesas sem dupla classificação | BRL | Opcional individualmente | Total, ranking e indicadores da categoria |
| custo_total | decimal ≥ 0 | Soma das sete categorias, derivada quando completas | BRL | Opcional na entrada | Conciliação e total financeiro |

## Regras de interpretação

CSV UTF-8, cabeçalho sem duplicatas; datas no formato AAAA-MM; não aceitar km negativos, infinito ou moeda textual inválida. XLSX usa primeira aba, sem células mescladas ou fórmulas para valores de entrada. Identificadores numéricos devem ser armazenados como texto quando houver zeros à esquerda. Valores monetários em reais correntes, não centavos. Vazio = desconhecido; zero = despesa declarada inexistente. Total não deve ser somado às categorias novamente.

Tipos sem benchmark são preservados e não comparados. Km zero não gera razão por km daquela linha. Litros ausentes bloqueiam L/100 km, mas não combustível em R$. Não estimar tributos/seguros anuais a partir de um pagamento isolado: padronizar competência antes da entrada.

## Dicionário do benchmark

| Nome | Tipo | Descrição | Unidade | Obrigatória | Utilização |
|---|---|---|---|---|---|
| tipo_veiculo | texto | Segmento simulado | categoria | Sim | Junção |
| categoria | texto | custo_combustivel ou custo_manutencao | categoria | Sim | Regra sem sobreposição |
| referencia_r_por_km | decimal > 0 | Referência didática | BRL/km | Sim | Custo comparável |
| origem | texto | SIMULADO_ACADEMICO | rótulo | Sim | Transparência |
| versao | inteiro | Versão do conjunto | versão | Sim | Rastreabilidade |

Cada par tipo/categoria é único. Produção adicionará região, segmento, validade, amostra, método e autorização de uso; não existem nesta versão.
