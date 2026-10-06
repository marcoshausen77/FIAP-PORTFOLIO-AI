# Roteiro do vídeo — até 5 minutos

Status: **não gravado / link pendente**. Duração planejada: **4min40s**, reservando 20 segundos até o limite. Narração humana ou legendas legíveis. Publicar no YouTube como **Não listado**. Não mostrar credenciais, e-mail de login, códigos ou telas de configuração da conta.

Antes de gravar: preencher nome do grupo, integrantes e tutor; abrir README, diagrama e aplicativo; carregar o exemplo. Ensaiar com cronômetro. Se ultrapassar cinco minutos, reduzir detalhes da demonstração.

| Tempo | Tela | Fala sugerida |
|---|---|---|
| 0:00–0:30 | Título e problema no README | “Este é o FleetSave AI, nossa proposta para o Enterprise Challenge da FIAP com a Sem Parar Empresas. Despesas de frota chegam por planilhas, sistemas e documentos. Sem consolidação, é difícil conhecer o custo da operação, priorizar problemas e estimar oportunidades de redução. A Sprint 1 constrói a base técnica e de negócio dessa solução.” |
| 0:30–1:15 | Usuários e seção das dez US | “Atendemos três perfis: o gestor de frota precisa agir; o CFO precisa decidir; e a Sem Parar Empresas precisa reconhecer necessidades aderentes. Estruturamos dez User Stories: consolidar despesas, identificar ineficiências, comparar benchmarks, estimar economia, lidar com dados incompletos, apresentar visão executiva, recomendar ações, acompanhar custos, mapear oportunidades e proteger os dados. Cada história tem necessidade, funcionalidade, critério de aceite, prioridade e Sprint prevista. Elas foram estruturadas pelo grupo a partir do briefing.” |
| 1:15–2:15 | Jornada e regras de negócio | “O usuário envia dados, revisa validações e recebe indicadores, diagnóstico e plano de ação. A economia vem de uma regra explicável: custo observado menos custo de referência para a mesma quilometragem, limitado a zero quando não houver excesso. Aplicamos um fator de realização de cenário. Por exemplo: novecentos reais de combustível em mil quilômetros, com referência de setenta e cinco centavos por quilômetro, geram cento e cinquenta reais de excesso teórico e setenta e cinco reais no cenário de cinquenta por cento. Referências são simuladas. Não prometemos economia real. Cada recomendação mostra evidência, impacto, prioridade e próximo passo. Produtos só aparecem quando há aderência lógica.” |
| 2:15–3:00 | Dataset e dicionário | “A base é inteiramente fictícia: oito veículos ao longo de seis meses, totalizando quarenta e oito registros. O dicionário define unidades e campos. Diferenciamos ausência de zero: se faltar quilometragem, por exemplo, o custo por quilômetro fica indisponível. Duplicatas e totais inconsistentes bloqueiam a análise. O relatório informa cobertura e limitações. Alta completude não significa certeza sobre o benchmark. Na evolução, referências deverão considerar histórico, tipo de veículo, região e segmento.” |
| 3:00–3:40 | Diagrama Mermaid e segurança | “A arquitetura separa ingestão, extração, validação, padronização, base de dados, indicadores, benchmark, diagnóstico e relatório. OCR e inteligência artificial ficam para próximas Sprints. A IA poderá extrair campos e explicar resultados, mas não inventará números financeiros. Planejamos autenticação, isolamento por empresa, menor privilégio, rastreabilidade e minimização de dados. O protótipo atual é local, não tem autenticação e utiliza apenas dados fictícios.” |
| 3:40–4:20 | MVP: exemplo, meses, cenário, relatório | “Como bônus, após concluir a documentação, implementamos um protótipo em Python, Pandas e Streamlit. Ele recebe CSV ou XLSX, valida dados e mostra custos, evolução e oportunidades simuladas. Aqui filtramos um mês e examinamos o benchmark e o plano de ação. Podemos ajustar o fator do cenário e baixar um relatório. A validação incluiu quarenta e seis testes aprovados e execução do Streamlit. PDF, OCR e integração comercial ainda não estão implementados.” |
| 4:20–4:40 | Roadmap e pendências | “As próximas Sprints evoluem pipeline, dashboard, referências validadas, dados não estruturados e segurança. Nossa base conecta problema, histórias, dados, fórmulas e ações com limitações claras. O repositório privado concentra documentação, código, testes e instruções de execução.” |

## Conferência antes de publicar

1. Usar nomes reais somente após confirmação do grupo.
2. Não confundir o bônus com um requisito obrigatório da Sprint 1.
3. Conferir tempo total, áudio ou legendas e legibilidade.
4. Publicar como **Não listado**, não como privado.
5. Testar o link sem autenticação de proprietário.
6. Inserir exatamente o mesmo link em `README.md` (seção 30) e `../../ENTREGA.txt`.
7. Atualizar checklist. Enviar ao Portal do Aluno apenas `ENTREGA.txt`, com os dois links completos.
