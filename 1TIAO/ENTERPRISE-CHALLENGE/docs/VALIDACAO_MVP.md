# Validação do bônus funcional

Execução em 06/10/2026 com Python 3.12, Pandas 2.2.3, Streamlit 1.50.0, openpyxl 3.1.5 e pytest 8.4.2.

## Resultado

`python -m pytest -q`: **46 testes passaram em 1,79 segundo** na execução final. O primeiro ciclo tinha 45 casos; foi adicionado um teste de arredondamento monetário decimal half-up. Suite inclui cálculos, ingestão e interface via AppTest.

| Grupo | Evidências |
|---|---|
| Financeiro | Total, custo/km ponderado, custo/veículo, consumo, zero, ausência e conciliação |
| Validação | Campo obrigatório, período inválido, negativo, infinito, NaN textual, duplicata e tipo conflitante |
| Benchmark | Cenário conhecido de R$ 75, zero de economia, cobertura parcial, tipo desconhecido, referência inválida, fator inválido |
| Recomendações | Evidência, prioridade e aderência; multas sem estimativa indevida de economia |
| Ingestão | CSV, XLSX equivalente, separador brasileiro, arquivo inválido, fórmulas XLSX e limite de tamanho |
| Streamlit | Exemplo completo, filtro mensal, visão CFO, fator zero, seleção vazia, upload CSV/XLSX e rejeição de entrada inválida |
| Relatório | Resumo, números, ações e ressalvas no Markdown exportável |

O Streamlit foi iniciado por `python -m streamlit run src/app.py`, em localhost; endpoint `/_stcore/health` respondeu **ok**. O servidor de verificação foi encerrado depois; não há URL pública ou serviço hospedado permanente.

O arquivo `frota_exemplo.csv` foi carregado no fluxo do aplicativo via Streamlit AppTest. Como a versão 1.50 não oferece operação nativa de upload no AppTest, os testes de upload injetam bytes no retorno de `file_uploader`; ingestão, validação, análise, renderização e exportação executam o código real. Não se alega teste manual de navegador nem teste de produção multiusuário.

## Resultado de referência — arquivo completo

| Métrica | Valor |
|---|---:|
| Empresa fictícia | EMP_DEMO_01 |
| Meses | janeiro–junho/2026 |
| Registros | 48 |
| Veículos | 8 |
| Km | 185.787 |
| Custo total | R$ 295.733,12 |
| Custo/km | R$ 1,5918 |
| Combustível | R$ 207.096,54 |
| Excesso teórico simulado | R$ 24.124,89 |
| Cenário a 50% (arredondado) | R$ 12.062,45 |
| Completude | 100% — ALTA |
| Recomendações | 8 |

A cobertura integral não valida o benchmark. Esses números são exclusivamente demonstrativos; economia real exigiria referência válida e aferição posterior.

## Limitações conhecidas

Sem OCR/PDF, IA, treino, banco, login, segregação de empresas por autorização, integração Sem Parar, envio de leads ou exportação PDF. Uma empresa por análise, custos em BRL e competência mensal. A seleção de empresa é filtro visual, não barreira de segurança. Os testes não garantem ausência de vulnerabilidades; uso restrito a simulação local.
