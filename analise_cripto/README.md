# Sistema de Auxílio à Tomada de Decisão para Investimento em Criptoativos

Este projeto tem como objetivo construir um sistema de auxílio à tomada de decisão para o investimento em criptoativos, com foco na análise de dados históricos de preços e na previsão dos melhores momentos para compra e venda. Utilizando técnicas de machine learning e análise de dados, o sistema analisará o comportamento dos preços de diferentes criptoativos e fornecerá insights valiosos para investidores.

O projeto inclui as seguintes etapas:
1. Exploração e Análise de Dados: Inicialmente, será realizada uma análise exploratória dos dados históricos de preços de criptoativos, como Bitcoin, EOS, e Solana. Isso inclui a identificação de padrões de comportamento e tendências ao longo do tempo, que podem ser úteis para a construção dos modelos preditivos.

2. Escolha de Modelos de Machine Learning: Após a análise dos dados, diferentes modelos de machine learning serão testados para prever os melhores momentos de compra e venda, com base nos padrões identificados.

3. Implementação de um Dashboard Interativo: Para facilitar o uso do sistema, será implementado um dashboard que permitirá aos usuários visualizar os resultados das previsões e interagir com o modelo, analisando diferentes cenários de investimento.

4. API para Acesso aos Resultados: O sistema também disponibilizará uma API, que permitirá o acesso aos resultados das previsões, além de possibilitar a integração com outros sistemas ou ferramentas de investimento.

## Dados Utilizados

Os dados históricos de preços foram coletados de criptoativos populares como:

- Bitcoin (BTC)
- EOS (EOS)
- Solana (SOL)

Esses dados estão armazenados na pasta data/raw e serão usados para realizar a análise exploratória e a construção dos modelos preditivos.

## Ferramentas Utilizadas

O projeto será desenvolvido utilizando as seguintes tecnologias e ferramentas:

    Python: Linguagem principal para a análise e modelagem dos dados.
    Pandas: Para manipulação e análise dos dados.
    Matplotlib/Seaborn: Para visualização de dados.
    Scikit-learn: Biblioteca de machine learning para implementação dos modelos preditivos.
    Jupyter Notebook: Para a exploração de dados e documentação.
    PostgreSQL: Para armazenamento dos dados.
    Docker: Para containerização do ambiente de desenvolvimento e do banco de dados.
    Dash/Plotly: Para criação de um dashboard interativo que exibirá os resultados dos modelos.

# 01 - Data Exploration

## Análise Inicial de Preços de Criptoativos

Neste notebook (analise_cripto/notebooks), foi realizado a exploração dos dados de preços de fechamento dos criptoativos Bitcoin, EOS, e Solana. O objetivo é entender o comportamento dos preços ao longo do tempo e identificar padrões relevantes para a construção de um modelo de machine learning que possa auxiliar na tomada de decisões de compra e venda.

### Análise do Gráfico de Preço do Bitcoin

O gráfico de preço de fechamento do Bitcoin mostra uma tendência de alta acentuada no ano de 2021, porém, seguida de uma queda abrupta na metade do mesmo ano. Por mais que essa moeda seja um investimento mais seguro e estável, esses picos e vales podem indicar momentos de grande volatilidade, que serão importantes para definir o melhor momento de compra e venda no futuro.

Segue o primeiro gráfico plotado:

### Análise do Gráfico de Preço do EOS

Diferentemente do Bitcoin, o preço de fechamento é bem menor, tendo uma alta em no início até o meio de 2018, entrando em queda até meio de 2021, porém, havia se estabilizado - mostrando apenas algumas alterações - durante o período de 2019 até início de 2021.

Segue o gráfico plotado:

### Análise do Gráfico de Preço da Solana

Por fim, a Solana, assim como a EOS, nçao possui preços elevados como o BitCoin. O gráfico exibe um crescimento de preço abrupto no meio do ano de 2021 e leve queda no segundo semestre.

Segue o gráfico:

### Análise da Matriz de Correlação e da Distribuição dos Preços de Fechamento do Bitcoin

#### Matriz de Correlação

- O volume de negociação (Volume) tem uma correlação moderada (entre 0.79 e 0.81) com os preços e a capitalização de mercado. Isso indica que, apesar de o volume não estar tão diretamente relacionado aos preços quanto as outras variáveis, ele ainda tem um impacto importante. Um aumento no volume de negociação pode estar associado a variações nos preços, mas não tão fortemente quanto as variações entre os próprios preços.

- A capitalização de mercado tem uma correlação forte (quase 1) com os preços de abertura, fechamento, alta e baixa. Isso é esperado, já que a capitalização de mercado depende diretamente do preço do ativo multiplicado pelo número de moedas em circulação. Ou seja, mudanças no preço do Bitcoin afetam imediatamente a capitalização de mercado.

- A Média Móvel de 30 dias também está fortemente correlacionada com os preços, o que é natural, já que a SMA é uma média dos preços ao longo do tempo. A alta correlação (próxima de 1) com High, Low, Open, e Close indica que a média móvel segue muito de perto o movimento dos preços.

- O SNo (provavelmente um número de série ou índice) tem uma correlação muito fraca com outras variáveis, o que faz sentido, pois ele é apenas um identificador e não está diretamente relacionado com o comportamento financeiro do Bitcoin.

Conclui-se que as variáveis de preço são altamente independentes, portanto, qualquer análise ou modelo preditivo que considere um desses preços pode incluir qualquer outro sem perda significativa de informação, visto que eles se movem em sincronia. O volume de negociação tem uma correlação mais baixa em relação aos preços e à capitalização de mercado, sugerindo que ele pode ser influenciado por outros fatores, como a liquidez do mercado, o sentimento do investidor, ou eventos externos que não estão diretamente ligados ao preç, sendo um indicativo não tão bom quanto a capitalização de mercado ou os valores de abertura/fechamento.

#### Distribuição dos Preços de Fechamento

Realizando a análise com fins de investimento, o gráfico indica que a maioria das negociações e fechamentos ocorreu em valores muito inferiores aos atuais máximos, sugerindo que os investidores podem ter se beneficiado significativamente ao longo do tempo com o aumento de valor.