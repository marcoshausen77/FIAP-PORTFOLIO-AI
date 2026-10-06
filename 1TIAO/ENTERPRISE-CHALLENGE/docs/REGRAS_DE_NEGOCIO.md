# Regras de negócio e rastreabilidade

## Cálculos

A análise sempre opera sobre uma empresa selecionada e um recorte mensal. Total de cada linha deriva das sete categorias completas; na presença de lacuna, pode usar total informado compatível com subtotal conhecido. Sem ambos, a linha fica sem total, nunca com zero. Categorias incompletas têm subtotal conhecido e contagem de linhas cobertas. Custos por veículo se referem ao período selecionado.

Razões agregadas usam soma numerador / soma denominador, com cobertura completa e denominador positivo. Não usar média das razões individuais. Custo/km não é calculado se algum total ou km está ausente. Zeros são válidos para totais, mas denominador zero torna a razão indisponível.

## Benchmark e oportunidade

Elegível: categoria preenchida, tipo com referência e km > 0. Agrupar por tipo e categoria antes da diferença. Excesso = max(0, soma custo − referência × soma km). Economia cenário = excesso × fator, padrão 0,5. Cobertura = linhas elegíveis / linhas totais do recorte para a categoria, expressa em percentual. Referência é simulada mesmo com 100% de cobertura; nunca declarar confiança estatística alta no resultado financeiro.

Cada referência deve ser finita, positiva, única e da categoria combustível/manutenção; benchmark inválido interrompe comparações. Sem pares comparáveis, economia é indisponível, não zero. Sem desvio em pares válidos, economia zero é um resultado válido. Não somar despesas de manutenção ao total e novamente na oportunidade. Somar oportunidades das duas categorias disjuntas; registrar eventual sobreposição de intervenções antes de usar em produção.

## Prioridade — parâmetros acadêmicos

- Alta: economia de cenário ≥ R$ 1.000 e cobertura ≥90%; ou multas conhecidas positivas, pela necessidade de revisar causas e prazos, sem presumir vencimento iminente.
- Média: economia ≥ R$ 300 e cobertura ≥60%; ou oportunidade positiva com cobertura ≥90%; ou conciliação de pedágio positivo.
- Baixa: demais oportunidades; coletar/validar dados antes de investir.

São limites didáticos por recorte, não limites da parceira. Dentro da prioridade, ordenar por economia conhecida. Multas e pedágio recebem economia indisponível, porque valor gasto não comprova economia alcançável. Falta de dados pode resultar só em recomendação de coleta, sem produto.

## Plano de ação

Cada item registra problema, evidência, impacto, recomendação, prioridade, economia estimada (ou indisponível), próximo passo, cobertura e possível aderência. O relatório não afirma que produto garante redução. Gestor confirma evidência e responsável antes de execução.

## Exemplos de aceite

1. Custo 900, km 1.000, referência 0,75: observado 0,90; excesso 150; cenário 75.
2. Custo 600 para a mesma exposição: excesso e cenário 0.
3. Km vazio: custo permanece conhecido, razão e benchmark daquela linha indisponíveis.
4. Todas as categorias zero e km 1.000: custo total e custo/km 0; participação percentual indisponível (divisor zero).
5. Custo total 100 com subtotal conhecido 120: bloquear conciliação.
6. Duas linhas da mesma empresa, veículo e mês: bloquear para evitar dupla contagem.
7. Um mês ausente: não criar mês com valor zero nem concluir redução.

## Atualização e impacto realizado

Futuro: importar nova versão, comparar chaves, revisar diferenças e gravar evento. Registrar ação com data e grupo afetado; comparar antes/depois por km e perfil equivalente. Economia realizada líquida deve descontar implantação e controlar volume/mix; redução bruta de despesa isolada não prova efeito. No bônus, recarregar arquivo substitui o anterior e a série vem apenas dos dados atuais.
