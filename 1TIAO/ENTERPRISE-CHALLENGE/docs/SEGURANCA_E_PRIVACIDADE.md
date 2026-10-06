# Segurança e privacidade

## Escopo e estado

Sprint 1: desenho de controles. Bônus: ferramenta local, dados simulados, arquivos limitados e validados, sem autenticação, sem banco, sem envio a LLM. Não publicar o MVP como serviço para dados reais. Repositório privado não substitui proteção da aplicação.

## Plano de controles

| Risco | Controle planejado | Evidência de aceite |
|---|---|---|
| Acesso indevido | OIDC, MFA administrativo e sessões com expiração | Sessão expirada nega acesso |
| Vazamento entre empresas | Autorização no servidor, tenant obrigatório em consultas e storage | Usuário A não consulta/exporta B, inclusive por ID direto |
| Privilégios excessivos | Gestor operacional, CFO leitura executiva, parceira só escopo permitido; revisão periódica | Matriz de papéis e testes negativos |
| Segredos no código | Cofre/ambiente; `.env` só local; `.gitignore`; varredura de segredos | Chave de teste proibida falha no gate |
| Dados alterados/duplicados | Hash, conciliação, chave e versão imutável de lote | Reimportação idempotente e trilha de correção |
| Upload malicioso | Limite de tamanho, formato, expansão XLSX; sandbox/antivírus futuros | Arquivos inválidos recusados sem execução |
| Vazamento em logs | Não registrar linhas brutas, tokens ou dados pessoais; controlar acesso | Logs de evento com IDs pseudônimos |
| Perda de dados | Backup cifrado, restauração testada, segregação de chaves | Ensaio de recuperação documentado |
| Uso indevido de IA | Não enviar PII por padrão; contratos e escopo de dados; revisão das saídas | Teste de extração sem obedecer instruções do documento |

## LGPD e minimização

A [Lei 13.709/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm) orienta a consideração de finalidade, necessidade e segurança no tratamento. Para produção, definir papéis de controlador/operador, finalidade e base legal por operação, transparência ao titular, retenção e atendimento de direitos, com revisão jurídica. Não presumir que consentimento é sempre a base adequada nem que pseudonimização equivale a anonimização.

Proposta do projeto: usar identificador de veículo, evitando nome de motorista, CPF, placa e localização precisa. Documentos futuros podem conter dados pessoais; prever mascaramento e acesso restrito. Benchmarks compartilhados devem avaliar risco de reidentificação em grupos pequenos e excluir agregados insuficientes. Finalidade comercial exige governança própria; o usuário não autoriza compartilhamento simplesmente ao importar um arquivo.

## Credenciais e integridade

API keys nunca devem ser versionadas, inclusive em notebooks, screenshots e histórico Git. `.env` e `.streamlit/secrets.toml` ficam ignorados; `.env.example` poderá conter somente nomes de variáveis, sem valores. Não há API key necessária no bônus. Em exposição acidental: revogar/rotacionar segredo e investigar alcance; apagar a linha não elimina o histórico.

Produção: TLS em trânsito, cifragem em repouso, chaves em cofre, controle de alterações e trilha de quem importou, corrigiu, consultou e exportou. Manter versão dos dados, benchmark, fórmula e relatório. Logs devem apoiar rastreabilidade com minimização.

## Retenção e incidentes — a validar

Política proposta: definir prazos contratuais por finalidade, exclusão de originais após a necessidade, expurgo seguro e tratamento de backups. Não existe prazo universal definido pelo projeto. Preparar canal de incidentes, contenção, preservação de evidências e avaliação de notificações segundo regras aplicáveis. Testar antes da produção.

## Bônus local

As entradas ficam em memória durante a sessão; não há persistência intencional do upload. Limites de 5 MB, 10.000 linhas e 50 colunas reduzem risco, mas não compõem sandbox de arquivos hostis. A opção de perfil não fornece autorização. Usar exclusivamente dados fictícios. Não alegar conformidade LGPD completa ou prontidão produtiva.
