# Auditoria final — FleetSave AI / Sprint 1

Data: 06/10/2026. **Parte técnica preparada e validada. Submissão acadêmica ainda pendente de informações e vídeo.**

## Estado confirmado

| Item | Resultado | Evidência |
|---|---|---|
| Repositório | https://github.com/marcoshausen77/FIAP-PORTFOLIO-AI | Criação na conta marcoshausen77 |
| Visibilidade | PRIVATE | Interface e metadados da integração |
| Branch | main | Interface e consulta de branches |
| Template oficial | Preservado | Usado somente para consulta e atribuição |
| User Stories | 10, US01 a US10 | README seção 11, descrição e todos os campos |
| Dataset | 48 registros simulados | 8 veículos × 6 meses, chave única e totais conciliados |
| Benchmark | Simulado | Rótulo e premissas no CSV, README e interface |
| MVP | Funcional localmente | CSV/XLSX, validação, métricas, gráficos, cenário, ações e relatório |
| Testes | 46 aprovados | pytest; detalhes em VALIDACAO_MVP.md |
| Streamlit | Iniciado; health ok | Exemplo carregado via AppTest; sem hospedagem permanente |
| fiap-tutoria | Acesso de colaborador confirmado | Convite inicialmente pendente; consulta posterior retornou permission=write |
| Vídeo | PENDENTE | Roteiro de 4min40s pronto; nenhuma URL inventada |
| ENTREGA.txt | Criado, incompleto | URL real do GitHub; falta vídeo |

## Rastreabilidade dos requisitos do briefing

| Seções do briefing | Atendimento | Evidência |
|---|---|---|
| 1–5: enunciado, dores, capacidades, valor e usuários | CONCLUÍDO | README 6–10 e 12–13 |
| 6: dez US e oito elementos por história | CONCLUÍDO | README 11 |
| 7: portfólio e aderência | CONCLUÍDO | README 22; recomendações sem oferta forçada |
| 8: novo GitHub privado e template | CONCLUÍDO | Repositório confirmado; estrutura adaptada |
| 9: acesso fiap-tutoria | CONCLUÍDO | permission=write em consulta após o convite |
| 10–12: nome e READMEs | CONCLUÍDO técnico | README raiz e 31 seções; identificação pendente |
| 13–14: dataset e dicionário | CONCLUÍDO | data/ e DICIONARIO_DE_DADOS.md |
| 15–17: entrada, lacunas e indicadores | CONCLUÍDO | README 15–18 e módulos testados |
| 18–21: benchmark, diagnóstico, economia e ações | CONCLUÍDO | README 19–22, regras e testes numéricos |
| 22–24: IA, arquitetura e segurança | CONCLUÍDO como planejamento | Arquitetura Mermaid; plano de privacidade; limites explícitos |
| 25–26: relatório e atualizações | CONCLUÍDO | Exportação Markdown e plano de atualização versionada |
| 27–28: roadmap e Kanban | CONCLUÍDO | PLANEJAMENTO_SPRINTS.md e KANBAN.md |
| 29–30: bônus e testes | CONCLUÍDO | Sete módulos, dependências e 46 testes |
| 31: vídeo | PARCIAL | Roteiro pronto; gravação/publicação pendentes |
| 32–33: TXT e links | PARCIAL | TXT criado; marcador de vídeo igual no README |
| 34: checklist | CONCLUÍDO | Estados e pendências explicitados |
| 35: critérios de qualidade | CONCLUÍDO como revisão | Problema → solução → US → dados → fórmulas → ações |
| 36: informações pendentes | CONCLUÍDO como marcação | Sem nomes/links inventados |
| 37–38: restrições e ordem | CONCLUÍDO técnico | Privado primeiro; documentação auditada em commit anterior ao MVP |
| 39: retorno final | Registrado nesta auditoria | Status, arquivos, execução e pendências |

## Validação documental

Conferência automatizada de 31 seções, dez US e campos por história; CSV com 48 chaves únicas e soma de categorias conciliada; referências locais existentes; sem credenciais. O histórico separa o commit documental `f885bc1` do bônus `2f612bb` e desta revisão final. O README central concentra a Sprint 1; documentos complementares detalham execução.

Testes via AppTest não equivalem a teste manual de navegador. Upload é injetado no widget no teste, mantendo o pipeline real. Não houve publicação de site, treinamento, OCR ou integração com sistemas reais. O aplicativo é demonstração local, não serviço produtivo.

## Pendências antes do envio ao Portal

1. Informar nome do grupo e nomes/links dos cinco integrantes (ou ajustar à composição real confirmada).
2. Informar tutor e decidir participação no FIAP NEXT.
3. Gravar vídeo com no máximo 5 minutos, narração humana ou legendas; publicar no YouTube como **não listado**.
4. Substituir `[LINK DO YOUTUBE PENDENTE]` no README e no ENTREGA.txt pelo mesmo link válido.
5. Revisar a entrega e enviar **somente ENTREGA.txt** no Portal do Aluno. Nenhum envio ao portal foi feito.

Não há pendência técnica de criação do repositório ou de documentação das US. O trabalho não deve ser chamado de pronto para submissão enquanto faltarem os itens acima.

## Arquivos criados

- `.gitignore`
- `1TIAO/ENTERPRISE-CHALLENGE/README.md`
- `1TIAO/ENTERPRISE-CHALLENGE/data/README.md`
- `1TIAO/ENTERPRISE-CHALLENGE/data/benchmark_simulado.csv`
- `1TIAO/ENTERPRISE-CHALLENGE/data/frota_exemplo.csv`
- `1TIAO/ENTERPRISE-CHALLENGE/docs/ARQUITETURA.md`
- `1TIAO/ENTERPRISE-CHALLENGE/docs/AUDITORIA_FINAL.md`
- `1TIAO/ENTERPRISE-CHALLENGE/docs/AUDITORIA_SPRINT1.md`
- `1TIAO/ENTERPRISE-CHALLENGE/docs/CHECKLIST_ENTREGA.md`
- `1TIAO/ENTERPRISE-CHALLENGE/docs/DICIONARIO_DE_DADOS.md`
- `1TIAO/ENTERPRISE-CHALLENGE/docs/KANBAN.md`
- `1TIAO/ENTERPRISE-CHALLENGE/docs/PLANEJAMENTO_SPRINTS.md`
- `1TIAO/ENTERPRISE-CHALLENGE/docs/REGRAS_DE_NEGOCIO.md`
- `1TIAO/ENTERPRISE-CHALLENGE/docs/ROTEIRO_VIDEO.md`
- `1TIAO/ENTERPRISE-CHALLENGE/docs/SEGURANCA_E_PRIVACIDADE.md`
- `1TIAO/ENTERPRISE-CHALLENGE/docs/VALIDACAO_MVP.md`
- `1TIAO/ENTERPRISE-CHALLENGE/requirements.txt`
- `1TIAO/ENTERPRISE-CHALLENGE/src/analysis.py`
- `1TIAO/ENTERPRISE-CHALLENGE/src/app.py`
- `1TIAO/ENTERPRISE-CHALLENGE/src/benchmark.py`
- `1TIAO/ENTERPRISE-CHALLENGE/src/ingestion.py`
- `1TIAO/ENTERPRISE-CHALLENGE/src/recommendations.py`
- `1TIAO/ENTERPRISE-CHALLENGE/src/utils.py`
- `1TIAO/ENTERPRISE-CHALLENGE/src/validation.py`
- `1TIAO/ENTERPRISE-CHALLENGE/tests/conftest.py`
- `1TIAO/ENTERPRISE-CHALLENGE/tests/test_app.py`
- `1TIAO/ENTERPRISE-CHALLENGE/tests/test_core.py`
- `ENTREGA.txt`
- `README.md`
