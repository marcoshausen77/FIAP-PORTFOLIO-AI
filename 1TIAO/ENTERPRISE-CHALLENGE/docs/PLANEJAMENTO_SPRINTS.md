# Planejamento das Sprints

Planejamento proposto pelo **Grupo 83**. Cada entrega exige documentação, testes e revisão, não apenas código. Segurança começa no desenho e é aprofundada na Sprint 6.

| Sprint | Escopo | User Stories | Dependências | Critério de saída |
|---|---|---|---|---|
| 1 | Problema, usuários, schema, regras, arquitetura e roadmap | US01–US10 especificadas | Briefing | Documentos auditados; pendências acadêmicas visíveis |
| 2 | Pipeline CSV/XLSX, chaves, validação e persistência inicial | US01, US05, US10 | Schema S1 | Casos inválidos e reimportação sem duplicação; início de isolamento |
| 3 | Indicadores, dashboard e série mensal | US02, US05, US06, US08 | Pipeline | Reconciliação de indicadores e totais; cobertura exibida |
| 4 | Benchmark validado, diagnóstico, cenários e ações | US02, US03, US04, US07, US08, US09 | Indicadores e acesso a referências | Comparações explicáveis; oportunidades sem dupla contagem |
| 5 | OCR, extração, classificação e explicação por IA | US01, US05, US07 | Amostras autorizadas e schema | Avaliação de campos, revisão humana e fidelidade numérica |
| 6 | Hardening, identidade, autorização, testes e privacidade | US10 e revisão US01–US09 | Ambiente integrado | Testes de isolamento, segurança e restauração; revisão de dados |
| Final | Integração, usabilidade, vídeo e apresentação | US01–US10 | Gates anteriores | Fluxo completo aprovado, vídeo e acesso da tutoria verificados |

## Bônus da Sprint 1

Protótipo local antecipa ingestão tabular, indicadores, benchmark simulado e recomendações. Não substitui entrega das Sprints futuras: não possui persistência, benchmark real, OCR ou segurança produtiva. Sua existência não fecha automaticamente histórias inteiras do backlog.

## Riscos e mitigação

| Risco | Efeito | Mitigação |
|---|---|---|
| Dados sem km | Razões e benchmark bloqueados | Diagnóstico parcial e pedido de km |
| Benchmark inadequado | Economia enganosa | Validar contexto e rotular simulação |
| Extração errada | Números incorretos | Revisão humana e conciliação |
| Atraso no acesso a API | Pipeline incompleto | CSV como contrato inicial; mocks identificados |
| Escopo excessivo | Documentação/entrega atrasadas | Priorizar S1 e separar bônus |
| Vídeo ausente | Entrega acadêmica incompleta | Gravar, publicar como não listado e inserir o link antes do TXT |

## Definition of Done

História com aceite demonstrado, código revisado quando aplicável, testes adequados, documentação atualizada, limitações declaradas e evidência anexada.

## Responsabilidades do Grupo 83

- **Marcos Rodrigues Czerner Hausen:** liderança técnica, arquitetura, regras de negócio, pipeline, integração do MVP e testes críticos.
- **Bernardo Akin Chiusoli Mendes:** dados simulados, dicionário, indicadores e apoio à validação de benchmarks.
- **Kelly Mendonça Pereira:** requisitos, User Stories, critérios de aceite, revisão documental e apoio à segurança/privacidade.
- **Murilo Silva Brito da Rocha:** interface, dashboard, gráficos, relatório e testes da experiência.
- **Vanira Alves da Silva:** comunicação, revisão da apresentação e narração do vídeo.
