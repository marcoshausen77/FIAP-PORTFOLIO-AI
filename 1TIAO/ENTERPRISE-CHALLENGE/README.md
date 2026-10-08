# 1. FleetSave AI

**Calculadora Inteligente de Redução de Custos de Frota**  
FIAP — Graduação ON em Inteligência Artificial · Enterprise Challenge · Sem Parar Empresas · Sprint 1.

> A Sprint 1 estabelece a base do projeto. Os dados e benchmarks utilizados são simulados, e o MVP local foi desenvolvido como complemento da proposta.

## 2. Nome do grupo

**Grupo 69**

## 3. Integrantes e responsabilidades

| Integrante | Responsabilidade principal |
|---|---|
| Bernardo Akin Chiusoli Mendes | Dados e indicadores: dataset simulado, dicionário de dados, apoio a benchmarks e conferência dos indicadores. |
| Vanira Alves da Silva | Comunicação e documentação: revisão executiva da apresentação e **narração do vídeo**. |
| Kelly Mendonça Pereira | Requisitos e qualidade: User Stories, critérios de aceite, revisão documental e apoio em segurança/privacidade. |
| **Marcos Rodrigues Czerner Hausen** | **Liderança técnica:** arquitetura, regras de negócio, pipeline de validação e análise, integração do MVP e testes críticos. |
| Murilo Silva Brito da Rocha | Interface e visualização: dashboard Streamlit, gráficos, exportação do relatório e apoio aos testes da interface. |

## 4. Tutor

—

## 5. Coordenador

André Godoi Chiovato

## 6. Descrição do projeto

O FleetSave AI propõe reunir despesas da frota, calcular indicadores com rastreabilidade e transformar desvios em um plano de ação. O usuário fornece dados da operação e recebe uma visão financeira, as limitações da análise e os próximos dados que precisa coletar. Regras matemáticas sustentam os números; a IA futura apoiará extração e explicação.

## 7. Contexto

O briefing apresenta a Sem Parar Empresas como operação da Corpay ligada a mobilidade, pagamentos, despesas e benefícios corporativos. Custos de combustível, manutenção, pedágio, multas, impostos e seguros chegam por sistemas, planilhas, PDFs, imagens, prints e extratos. O desafio é converter essa fragmentação em informação utilizável por gestores e liderança.

As User Stories foram estruturadas pelo grupo com base nas necessidades apresentadas no briefing do Challenge.

## 8. Problema

| Dor | Consequência | Resposta proposta |
|---|---|---|
| Fontes e formatos distintos | Retrabalho e registros duplicados | Ingestão, schema e chave única |
| Categorias não consolidadas | Custo total desconhecido | Taxonomia e soma conciliada |
| Prioridades pouco claras | Esforço em gastos de baixo impacto | Ranking financeiro e evidências |
| Ausência de comparação | Custo elevado confundido com ineficiência | Benchmark comparável e documentado |
| Diagnóstico sem ação | Informação sem mudança operacional | Plano com responsável, prazo e próximo passo |
| Economia sem método | Decisões com falsa precisão | Fórmulas, exposição e cenários explícitos |

## 9. Objetivos

Consolidar despesas por empresa, veículo e mês; reconhecer lacunas; priorizar desvios comparáveis; estimar oportunidades em reais; recomendar ações verificáveis; acompanhar resultados. A base da Sprint 1 deve permitir que outra equipe implemente e teste o desenho sem precisar adivinhar unidades, regras ou limites.

Critérios de sucesso acadêmico: dez histórias rastreáveis, schema coerente, nenhuma ausência transformada silenciosamente em zero, fórmulas reproduzíveis, distinção entre planejado e implementado e execução documentada. Metas de negócio (valores-alvo a validar com a parceira): tempo de diagnóstico, percentual de importações válidas, ações adotadas e economia realizada líquida.

## 10. Usuários

| Perfil | Necessidades | Visão prevista |
|---|---|---|
| Gestor de Frota | Total, desperdícios, prioridades, ações e evolução | Indicadores operacionais, cobertura e plano de ação |
| CFO / Liderança | Impacto, potencial e decisões | Resumo executivo, exposição e limitações |
| Sem Parar Empresas | Necessidades, oportunidades e inteligência | Necessidades aderentes e agregados autorizados |

A seleção de perfil do MVP muda a apresentação; não é autenticação nem autorização.

## 11. User Stories

User Stories selecionadas e estruturadas pelo grupo com base nas necessidades apresentadas no briefing do Challenge.

Todas são especificadas na Sprint 1; a coluna Sprint indica a implementação planejada. O bônus antecipa partes dessas funcionalidades, sem concluir controles de produção.

### US01 — Consolidação de despesas

Como Gestor de Frota, quero enviar dados de custos provenientes de diferentes fontes, para visualizar o custo consolidado da minha operação.

| Campo | Definição |
|---|---|
| Perfil | Gestor de Frota |
| Necessidade | Reunir fontes dispersas sem dupla contagem. |
| Funcionalidade | Importação e consolidação |
| Critério de aceite conceitual | Dado um arquivo válido e outro com a mesma chave, quando importados, então os registros válidos são consolidados e a duplicidade é bloqueada, com explicação. |
| Prioridade | Alta |
| Sprint prevista | 2 |

### US02 — Identificação de ineficiências

Como Gestor de Frota, quero identificar quais categorias apresentam maior impacto ou possíveis ineficiências, para saber onde devo agir primeiro.

| Campo | Definição |
|---|---|
| Perfil | Gestor de Frota |
| Necessidade | Distinguir maior gasto de ineficiência comprovada. |
| Funcionalidade | Ranking e desvios |
| Critério de aceite conceitual | Dadas categorias com custos válidos, o ranking mostra valores e participações; uma categoria só recebe sinal de desvio se houver referência comparável e exposição válida. |
| Prioridade | Alta |
| Sprint prevista | 3–4 |

### US03 — Benchmark

Como Gestor de Frota, quero comparar os indicadores da minha operação com referências, para identificar custos fora do comportamento esperado.

| Campo | Definição |
|---|---|
| Perfil | Gestor de Frota |
| Necessidade | Comparar operações equivalentes. |
| Funcionalidade | Benchmark segmentado |
| Critério de aceite conceitual | Dado um tipo com referência, exibir observado, referência, unidade e origem; sem referência, mostrar indisponível, sem substituir por outro tipo. |
| Prioridade | Alta |
| Sprint prevista | 4 |

### US04 — Economia potencial

Como Gestor de Frota, quero visualizar uma estimativa de economia potencial em reais, para compreender o impacto financeiro das oportunidades identificadas.

| Campo | Definição |
|---|---|
| Perfil | Gestor de Frota |
| Necessidade | Dimensionar oportunidades financeiras. |
| Funcionalidade | Estimativa determinística |
| Critério de aceite conceitual | Dado combustível de R$ 900, 1.000 km e referência R$ 0,75/km, mostrar R$ 150 de excesso teórico e R$ 75 de cenário realizável a 50%, com premissas. |
| Prioridade | Alta |
| Sprint prevista | 4 |

### US05 — Dados incompletos

Como Gestor de Frota, quero obter um diagnóstico mesmo quando ainda não possuir todas as informações, para receber uma análise inicial e saber quais dados devo fornecer posteriormente.

| Campo | Definição |
|---|---|
| Perfil | Gestor de Frota |
| Necessidade | Analisar sem falsa precisão. |
| Funcionalidade | Completude e limitações |
| Critério de aceite conceitual | Dado km ausente, manter os custos conhecidos, sinalizar ausência e impedir custo/km e economia baseada em km; custo desconhecido não vira zero. |
| Prioridade | Alta |
| Sprint prevista | 2–3 |

### US06 — Visão executiva

Como CFO ou integrante da liderança, quero visualizar um resumo executivo com custo total, principais ineficiências, economia potencial e prioridades, para apoiar decisões financeiras.

| Campo | Definição |
|---|---|
| Perfil | CFO / Liderança |
| Necessidade | Decidir com visão executiva. |
| Funcionalidade | Painel executivo e relatório |
| Critério de aceite conceitual | Dada análise válida, resumo apresenta período, total ou subtotal identificado, categorias, oportunidade, prioridades, cobertura e ressalvas. |
| Prioridade | Alta |
| Sprint prevista | 3–4 |

### US07 — Plano de ação

Como Gestor de Frota, quero receber recomendações organizadas por prioridade e impacto, para transformar o diagnóstico em ações práticas.

| Campo | Definição |
|---|---|
| Perfil | Gestor de Frota |
| Necessidade | Converter evidências em ações. |
| Funcionalidade | Plano de ação explicável |
| Critério de aceite conceitual | Dado desvio positivo, cada recomendação apresenta problema, evidência, impacto, ação, prioridade, economia e próximo passo; sem desvio não há economia inventada. |
| Prioridade | Alta |
| Sprint prevista | 4 |

### US08 — Acompanhamento dos custos

Como Gestor de Frota, quero acompanhar os custos ao longo do tempo, para verificar se as ações adotadas estão produzindo resultados.

| Campo | Definição |
|---|---|
| Perfil | Gestor de Frota |
| Necessidade | Verificar evolução e resultado. |
| Funcionalidade | Série mensal e atualização |
| Critério de aceite conceitual | Dados dois meses válidos, mostrar a série em ordem e o custo/km quando possível; mudança na frota impede atribuir toda diferença a uma ação. Reimportação não duplica períodos. |
| Prioridade | Média |
| Sprint prevista | 3–4 |

### US09 — Oportunidades Sem Parar Empresas

Como Sem Parar Empresas, quero identificar oportunidades observadas no diagnóstico, para apresentar soluções adequadas ao problema do cliente quando houver aderência.

| Campo | Definição |
|---|---|
| Perfil | Sem Parar Empresas |
| Necessidade | Identificar necessidades aderentes. |
| Funcionalidade | Mapeamento de oportunidades |
| Critério de aceite conceitual | Dado desvio de combustível, sugerir avaliar Multiabastece; sem aderência, não ofertar produto. Visão comercial só usa escopo autorizado e não envia leads automaticamente. |
| Prioridade | Média |
| Sprint prevista | 4–6 |

### US10 — Segurança e privacidade

Como cliente, quero que meus dados sejam tratados de maneira segura e responsável, para proteger informações empresariais e pessoais.

| Campo | Definição |
|---|---|
| Perfil | Cliente |
| Necessidade | Proteger dados empresariais e pessoais. |
| Funcionalidade | Acesso, minimização e auditoria |
| Critério de aceite conceitual | Em ambiente produtivo planejado, usuário de empresa A não acessa dados de B; segredos não entram no Git; acessos e exportações são auditáveis. MVP usa apenas simulação local. |
| Prioridade | Alta |
| Sprint prevista | 2–6 |


## 12. Solução proposta

Jornada: selecionar período → enviar arquivo → revisar validações e campos faltantes → consultar indicadores → examinar desvios → avaliar plano de ação → exportar resumo → atualizar dados no mês seguinte.

| Capacidade | Sprint 1 / bônus | Evolução planejada |
|---|---|---|
| CSV e XLSX padronizados | MVP após documentação | Mapeamento assistido de colunas |
| PDF, imagem, print, texto e extrato | Somente especificação | OCR e revisão humana |
| Cálculos e recomendações | Regras determinísticas | Parâmetros validados pela parceira |
| Benchmark | Simulado, segmentado por tipo | Histórico e referências validadas |
| Exportação | Relatório Markdown simples | PDF executivo com versionamento |
| Histórico | Série do arquivo carregado | Persistência e atualização incremental |
| Segurança | Uso local e dados fictícios | Identidade, isolamento, auditoria e criptografia |
| IA | Sem LLM ou treinamento | Extração, anomalias e explicação controlada |

## 13. Benefícios

Gestores podem concentrar esforço nas categorias mais relevantes; CFOs conseguem enxergar a exposição financeira e distinguir hipótese de resultado. Para a Sem Parar Empresas, o diagnóstico pode qualificar leads por necessidade, incentivar recorrência mensal, orientar o portfólio e permitir benchmarks agregados futuros. Isso depende de adesão, qualidade de dados e validação das recomendações. O MVP não coleta contatos nem envia leads.

## 14. Dados utilizados

[data/frota_exemplo.csv](data/frota_exemplo.csv): empresa fictícia **Logística Horizonte Demo**, identificador `EMP_DEMO_01`, oito veículos, três tipos e seis meses (janeiro a junho de 2026), 48 registros. Cada linha é um veículo em um mês, não uma transação. Impostos e seguro são apropriados mensalmente; não misturar regime de caixa com competência.

Não há placas, motoristas, CPF, clientes reais ou dados da Sem Parar. [Dicionário](docs/DICIONARIO_DE_DADOS.md) e [proveniência e premissas](data/README.md) detalham unidades, campos e geração. `custo_total` é soma das sete categorias; nunca somar esse campo novamente às categorias.

## 15. Estratégia de entrada

Fontes futuras: CSV, Excel, PDF, imagens, prints, textos, extratos e APIs. Entrada → extração → identificação dos campos → padronização → validação → classificação → armazenamento → análise. O desenho tem validação bruta antes e validação semântica depois da padronização.

No MVP: apenas CSV UTF-8 (vírgula/ponto decimal ou ponto e vírgula/vírgula decimal) e XLSX, primeira aba, cabeçalho único. Limites: 5 MB de arquivo, 10.000 linhas, 50 colunas; XLSX compactado tem limite adicional de conteúdo expandido. Ausência de colunas opcionais gera alerta. Cabeçalhos são normalizados para minúsculas, sem acentos e com sublinhados. Não há OCR, PDF ou API implementados.

## 16. Tratamento e padronização

Chave: `(empresa_id, veiculo_id, periodo)`. Identificadores são texto; período `AAAA-MM`; valores finitos e não negativos; números CSV seguem um único locale por arquivo. Duplicatas bloqueiam análise; linhas inválidas não são descartadas silenciosamente. Um veículo deve manter seu tipo no arquivo. Total informado é conciliado com categorias completas com tolerância de R$ 0,01 por registro. Se faltam categorias, custo total informado deve ser pelo menos o subtotal conhecido.

Zero significa valor conhecido igual a zero; vazio significa desconhecido. Colunas não reconhecidas são ignoradas com aviso. Mais de uma empresa no arquivo exige seleção antes da análise. Classificação automática de descrições livres fica para Sprint 5.

## 17. Dados incompletos

Completude = células preenchidas / células esperadas em tipo, km, litros e sete categorias de custo. Chaves são obrigatórias e o total derivável não entra no denominador. Alta: ≥90%; média: ≥60% e <90%; baixa: <60%. Essa classificação expressa cobertura, não certeza estatística nem qualidade do benchmark.

Toda análise informa campos recebidos, ausências por coluna, cálculos possíveis e bloqueados, limitações e coleta recomendada. Uma categoria só tem agregado integral se todas as linhas tiverem seu valor; caso contrário exibe apenas subtotal conhecido com esse rótulo. Total integral exige todas as linhas totalizadas (categorias completas ou total informado conciliável). Indicadores por km precisam de numerador e denominador completos e km total positivo. Benchmark usa só pares válidos custo/km/tipo e informa cobertura; tipos sem referência são excluídos, não substituídos.

## 18. Indicadores

| Indicador | Fórmula e condição |
|---|---|
| Custo total | Soma dos totais válidos; sem cobertura integral, indisponível e subtotal separado |
| Custo por veículo | Total / veículos distintos no recorte; é custo acumulado do período |
| Custo por km | Total / soma km, com todos os dados e km > 0 |
| Combustível total | Soma completa da categoria |
| Combustível por km | Soma custo combustível / soma km (R$/km) |
| Consumo físico | Soma litros / soma km × 100 (L/100 km); não média simples das razões |
| Manutenção por veículo | Soma manutenção / veículos distintos |
| Pedágio por km | Soma pedágio / soma km |
| Multas por veículo | Soma multas / veículos distintos |
| Participação | Categoria integral / total integral × 100; total > 0 |
| Evolução mensal | Totais por mês e custo/km quando os dados permitem |
| Maiores categorias | Ranking dos valores conhecidos, indicando cobertura |
| Desvio | Observado − referência na mesma unidade, tipo e exposição |

Meses ausentes não viram custo zero. O denominador por veículo conta cada veículo uma vez no período. Para decisão mensal, selecionar o mês. A evolução não comprova causalidade: volume, mix, região e sazonalidade devem ser controlados.

## 19. Diagnóstico

Consolidar → calcular métricas → comparar categorias → identificar desvios → medir impacto → estimar oportunidade → priorizar. Custos altos indicam materialidade, não fraude nem desperdício comprovado. O MVP compara combustível e manutenção em R$/km por tipo; outras categorias recebem orientação qualitativa sem economia fabricada. Toda oportunidade expõe tipo, categoria, custo observado, km elegíveis, referência, diferença e cobertura.

## 20. Benchmark

**Os benchmarks utilizados nesta Sprint são simulados e possuem finalidade exclusivamente acadêmica e demonstrativa. Em ambiente produtivo deverão ser substituídos por referências validadas.**

[data/benchmark_simulado.csv](data/benchmark_simulado.csv) contém valores didáticos de combustível e manutenção em R$/km para leve, van e caminhão. Zero referência não é permitido; tipos desconhecidos ficam sem comparação. Não são médias de mercado ou dados da Sem Parar.

Evolução: validar referência pelo histórico do cliente, tipo, porte, região, segmento, combustível, carga e janela temporal; considerar agregados com proteção de privacidade e aval da parceira. Versionar origem, validade, amostra e método. Diferenças de contexto podem invalidar comparações mesmo quando o tipo coincide.

## 21. Economia potencial

Para cada combinação categoria/tipo no recorte elegível:

`taxa_observada = custo_elegivel / km_elegiveis`

`excesso_teorico = max(0, taxa_observada - taxa_referencia) × km_elegiveis`

`economia_cenario = excesso_teorico × fator_realizacao`

Fator padrão didático = 50%, ajustável de 0% a 100%. Exemplo: R$ 900 / 1.000 km = R$ 0,90/km; referência R$ 0,75/km; excesso R$ 150; cenário a 50% = R$ 75. Não multiplicar novamente por km após calcular o excesso monetário.

Somam-se apenas categorias disjuntas (combustível e manutenção), sem somar também custo total. Agregar primeiro dentro do mesmo tipo/categoria evita somar somente linhas desfavoráveis. Não extrapolar linhas excluídas nem anualizar seis meses sem premissa. Cenário não é economia garantida, líquida ou comprovada: faltam custos de implantação, sazonalidade e validação operacional. A IA não gera esses números.

## 22. Recomendações

Formato: problema → evidência → impacto → recomendação → prioridade → economia estimada → próximo passo. Ordenação considera valor financeiro, cobertura e urgência; [regras detalhadas](docs/REGRAS_DE_NEGOCIO.md).

| Evidência | Ação e próximo passo | Possível aderência |
|---|---|---|
| Combustível acima da referência simulada | Conferir preço, abastecimentos e rotas; testar intervenção e medir | Avaliar Multiabastece |
| Manutenção acima da referência simulada | Conferir ordens, causas e plano preventivo; investigar antes de cortar | Avaliar Gestão de Manutenção |
| Pedágio relevante | Conciliar rota, passagens e cobranças; verificar contexto da operação | Avaliar Tag Sem Parar ou Vale-Pedágio conforme caso |
| Multas > 0 | Revisar causas, vencimentos e medidas educativas | Avaliar Gestor de Multas |
| Impostos, seguro e outros | Conciliar documentação e contratos | Sem oferta automática |

Antecipação de Recebíveis, Seguros, Transporte, VR+VA e Multi compõem o portfólio mencionado no briefing, mas o dataset não comprova necessidade desses produtos. Não são recomendados automaticamente. A aderência é uma hipótese comercial a validar; nenhum produto recebe promessa de desconto ou economia.

## 23. IA / Data Science / Automação

OCR futuro lê documentos; extração inteligente identifica campos; classificação sugere categorias com revisão; Data Science investiga padrões e anomalias; IA generativa explica resultados já calculados. Regras determinísticas permanecem responsáveis pelos cálculos financeiros. Não há treino de modelo, uso de LLM nem chamada externa de IA na Sprint 1.

Documentos podem conter instruções maliciosas: tratá-los como dados, limitar saídas ao schema e não executar instruções extraídas. Preservar trecho de origem e confiança de extração. Avaliar OCR por acurácia de campos; classificação por precisão/recall; explicação por fidelidade ao cálculo, não por fluência.

## 24. Arquitetura

[Diagrama e componentes](docs/ARQUITETURA.md). MVP: Streamlit → Pandas → validação → indicadores → benchmark local → recomendações → relatório. Dados ficam em memória. Produção: identidade, API autenticada, armazenamento de originais, banco por tenant, filas de extração, motor financeiro e relatórios auditáveis. OCR e LLM são serviços futuros separados do motor de cálculo.

## 25. Segurança e privacidade

[Plano de segurança](docs/SEGURANCA_E_PRIVACIDADE.md): autenticação, autorização por empresa, menor privilégio, integridade, logs minimizados, retenção e resposta a incidentes. Segredos fora do Git, via ambiente ou cofre; `.env` ignorado. O MVP não tem autenticação nem isolamento multiusuário: executar localmente, somente com dados fictícios, sem publicação pública. LGPD é requisito de desenho; não se declara conformidade produtiva por ter documentação.

## 26. Roadmap

[Planejamento das Sprints](docs/PLANEJAMENTO_SPRINTS.md) e [Kanban](docs/KANBAN.md). Na atualização futura: importar lote → validar → comparar chaves → revisar correções → gravar versão sem duplicar → recalcular → comparar janelas equivalentes → registrar ações. Histórico de versões permite reproduzir o relatório e diferenciar mudanças de dados de mudanças reais na operação.

Relatório futuro PDF: resumo executivo, período, total, categorias, ineficiências, cenários de economia, recomendações, prioridades, confiança/cobertura, fontes e versão. MVP exporta Markdown com esses elementos disponíveis. Recorrência mensal e avaliação das ações fecham o ciclo.

## 27. Estrutura do repositório

- `../../README.md`: portfólio FIAP e acesso à entrega.
- `../../assets/repositorio_privado.jpg`: evidência visual da privacidade do repositório.
- `README.md`: documentação central da Sprint 1.
- `data/`: frota, benchmark e premissas simuladas.
- `docs/`: dicionário, arquitetura, regras, segurança, Sprints, Kanban, auditoria, checklist e roteiro.
- `src/`: `app.py`, `ingestion.py`, `validation.py`, `analysis.py`, `benchmark.py`, `recommendations.py`, `utils.py`.
- `tests/`: testes financeiros, de validação, ingestão e integração Streamlit.
- `requirements.txt`: dependências do MVP e testes.
- `../../.gitignore`: exclusão de segredos, ambientes e dados privados.
- `../../ENTREGA.txt`: arquivo de entrega para o Portal FIAP.

Não foram criadas pastas vazias sem finalidade.

## 28. Decisões técnicas

Python 3.11+ (compatível com 3.12), Pandas para tabelas, Streamlit para interface local e openpyxl para XLSX. Separação de ingestão, validação, cálculo e apresentação facilita testar fórmulas. Valores de moeda são arredondados a centavos na apresentação com regra decimal half-up; tolerância de conciliação explícita. Banco, OCR e modelo de IA seriam custo e risco sem benefício para o planejamento desta Sprint; permanecem no roadmap.

CSV simulado é pequeno, legível e versionável. Referências em arquivo separado permitem trocar parâmetros sem alterar a fórmula. A versão do cenário e as limitações aparecem no relatório. Não se usam médias simples de custo/km para consolidar a frota.

## 29. Como executar o MVP

O MVP foi desenvolvido como complemento da documentação da Sprint 1. Requisitos: Python 3.11 ou 3.12 e Git. Na primeira execução, é necessária conexão apenas para instalar as dependências.

```bash
git clone https://github.com/marcoshausen77/FIAP-PORTFOLIO-AI.git
cd FIAP-PORTFOLIO-AI/1TIAO/ENTERPRISE-CHALLENGE
python -m venv .venv
```

No Windows PowerShell: `.venv\Scripts\Activate.ps1` (ou use diretamente `.venv\Scripts\python.exe`). No Linux/macOS: `source .venv/bin/activate`.

```bash
python -m pip install -r requirements.txt
python -m pytest -q
python -m streamlit run src/app.py --server.address 127.0.0.1
```

Abra `http://localhost:8501`. Clique **Carregar exemplo simulado** ou envie `data/frota_exemplo.csv`. Para XLSX, salve as mesmas colunas em uma primeira aba com células numéricas. Selecione empresa, meses e perfil; revise a qualidade; consulte gráficos, cenário e recomendações; baixe o relatório. Para parar, Ctrl+C no terminal.

Não há OCR, login, persistência, integração comercial ou publicação hospedada. Detalhes de execução e limitações dos testes estão em [VALIDACAO_MVP.md](docs/VALIDACAO_MVP.md).

## 30. Vídeo

Apresentação do projeto com narração de **Vanira Alves da Silva**:

https://youtu.be/lCkc8i8w0CQ

Vídeo publicado no YouTube como **não listado**, conforme os requisitos da entrega.

## 31. Participação no FIAP NEXT

**[x] Não vamos participar.**

## Referências e atribuição

- [Documentação Streamlit](https://docs.streamlit.io/develop/api-reference/app-testing): referência para testes da aplicação.
- [LGPD — Lei 13.709/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm): base legal a considerar no desenho de privacidade, sem substituir revisão jurídica.
- Briefing do Challenge: referência para o escopo, usuários, necessidades, produtos e requisitos de entrega. As dez User Stories foram estruturadas pelo grupo a partir dessas necessidades. Dados e referências numéricas foram criados exclusivamente para demonstração.
