# 01 - Data Exploration

## Análise Inicial de Preços de Criptoativos

Neste notebook (analise_cripto/notebooks), foi realizado a exploração dos dados de preços de fechamento dos criptoativos Bitcoin, EOS, e Solana. O objetivo é entender o comportamento dos preços ao longo do tempo e identificar padrões relevantes para a construção de um modelo de machine learning que possa auxiliar na tomada de decisões de compra e venda.

### Análise do Gráfico de Preço do Bitcoin

O gráfico de preço de fechamento do Bitcoin mostra uma tendência de alta acentuada no ano de 2021, porém, seguida de uma queda abrupta na metade do mesmo ano. Por mais que essa moeda seja um investimento mais seguro e estável, esses picos e vales podem indicar momentos de grande volatilidade, que serão importantes para definir o melhor momento de compra e venda no futuro.

Segue o primeiro gráfico plotado:

![Bitcoin](assets/images/bitcoin.png)

### Análise do Gráfico de Preço do EOS

Diferentemente do Bitcoin, o preço de fechamento é bem menor, tendo uma alta em no início até o meio de 2018, entrando em queda até meio de 2021, porém, havia se estabilizado - mostrando apenas algumas alterações - durante o período de 2019 até início de 2021.

Segue o gráfico plotado:

![EOS](assets/images/eos.png)

### Análise do Gráfico de Preço da Solana

Por fim, a Solana, assim como a EOS, nçao possui preços elevados como o BitCoin. O gráfico exibe um crescimento de preço abrupto no meio do ano de 2021 e leve queda no segundo semestre.

Segue o gráfico:

![Solana](assets/images/solana.png)

### Análise da Matriz de Correlação e da Distribuição dos Preços de Fechamento do Bitcoin

#### Matriz de Correlação

- O volume de negociação (Volume) tem uma correlação moderada (entre 0.79 e 0.81) com os preços e a capitalização de mercado. Isso indica que, apesar de o volume não estar tão diretamente relacionado aos preços quanto as outras variáveis, ele ainda tem um impacto importante. Um aumento no volume de negociação pode estar associado a variações nos preços, mas não tão fortemente quanto as variações entre os próprios preços.

- A capitalização de mercado tem uma correlação forte (quase 1) com os preços de abertura, fechamento, alta e baixa. Isso é esperado, já que a capitalização de mercado depende diretamente do preço do ativo multiplicado pelo número de moedas em circulação. Ou seja, mudanças no preço do Bitcoin afetam imediatamente a capitalização de mercado.

- A Média Móvel de 30 dias também está fortemente correlacionada com os preços, o que é natural, já que a SMA é uma média dos preços ao longo do tempo. A alta correlação (próxima de 1) com High, Low, Open, e Close indica que a média móvel segue muito de perto o movimento dos preços.

- O SNo (provavelmente um número de série ou índice) tem uma correlação muito fraca com outras variáveis, o que faz sentido, pois ele é apenas um identificador e não está diretamente relacionado com o comportamento financeiro do Bitcoin.

Conclui-se que as variáveis de preço são altamente independentes, portanto, qualquer análise ou modelo preditivo que considere um desses preços pode incluir qualquer outro sem perda significativa de informação, visto que eles se movem em sincronia. O volume de negociação tem uma correlação mais baixa em relação aos preços e à capitalização de mercado, sugerindo que ele pode ser influenciado por outros fatores, como a liquidez do mercado, o sentimento do investidor, ou eventos externos que não estão diretamente ligados ao preç, sendo um indicativo não tão bom quanto a capitalização de mercado ou os valores de abertura/fechamento.

![Matriz de Correlação](assets/images/matriz.png)

#### Distribuição dos Preços de Fechamento

Realizando a análise com fins de investimento, o gráfico indica que a maioria das negociações e fechamentos ocorreu em valores muito inferiores aos atuais máximos, sugerindo que os investidores podem ter se beneficiado significativamente ao longo do tempo com o aumento de valor.

![Distribuição dos Preços](assets/images/price.png)

# 02 - Feature Selection

## Seleção das Features

As features selecionadas para o modelo incluem:

- Preço de Abertura (Open)
- Preço Alto (High)
- Preço Baixo (Low)
- Volume de Negócios (Volume)

Essas features foram escolhidas com base em sua relevância em prever o preço de fechamento das criptomoedas, utilizando o preço de fechamento (Close) como variável alvo.

## Escolha do Modelo

O modelo escolhido para prever os preços de fechamento das criptomoedas é o Random Forest. Esta escolha foi baseada nos seguintes fatores:

- Robustez: O Random Forest é conhecido por sua capacidade de lidar com dados ruidosos e outliers, o que é especialmente importante em dados de mercado financeiro.
- Precisão: A combinação de múltiplas árvores de decisão tende a fornecer previsões mais precisas, minimizando o risco de overfitting.
- Importância das Features: O modelo permite calcular a importância das features, ajudando na interpretação dos resultados e na seleção de variáveis significativas.

## Resultados e Conslução

Após treinar e executar o modelo (resultados podem ser consultado em notebooks/02-feature-selection.ipynb)

## Resultados e Conclusões

Os resultados indicam que o modelo Random Forest pode prever o preço de fechamento com uma precisão razoável. Os RMSE para cada criptomoeda foram:

1. Bitcoin: 123.64
2. EOS: 0.27
3. Solana: 0.32

Com a escolha do Random Forest e a realização de um ajuste de hiperparâmetros, foi melhorado a previsão de preços de fechamento. Para futuras iterações, considera-se a inclusão de novas features ou o uso de outros modelos para comparar desempenhos.