# Dados inteiramente simulados

Empresa fictícia: Logística Horizonte Demo. 8 veículos × 6 meses = 48 linhas. Período janeiro–junho/2026. Semente de geração: 42. Não representam operação da Sem Parar, seus clientes ou média de mercado.

Uma linha por empresa/veículo/mês. Três leves, três vans e dois caminhões. Quilometragem em torno de 2.300, 3.800 e 6.200 km/mês respectivamente, variando entre 86% e 115%. Consumo-base didático: 11,5; 8,0; 3,7 km/L. Veículos 2 e 7 têm consumo maior para permitir investigação. Preço fictício: R$ 6,10/L (leve/van) e R$ 6,05/L (caminhão). Esses valores não são cotações.

Manutenção varia por exposição; van 5 tem despesa excepcional em março/abril. Pedágio proporcional a km no cenário; multas esparsas de R$ 195,23. Impostos e seguro apropriados mensalmente; outros custos pequenos. Total soma combustível, pedágio, manutenção, multas, impostos, seguro e outros. Nenhum total inclui custo de aquisição ou depreciação: o escopo é despesa operacional informada, não TCO completo.

`benchmark_simulado.csv`: seis referências, uma por tipo e categoria (combustível/manutenção), em R$/km, versão 1. Os benchmarks utilizados nesta Sprint são simulados e possuem finalidade exclusivamente acadêmica e demonstrativa. Em ambiente produtivo deverão ser substituídos por referências validadas.

Para XLSX, converter as mesmas colunas para uma planilha com uma primeira aba e números como células numéricas. Não usar totalizadores adicionais como linhas. Campos em branco são desconhecidos, nunca zeros implícitos. Arquivos reais não devem ser versionados.
