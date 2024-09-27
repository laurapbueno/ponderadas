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

# Estrutura de Pastas

---------------------
    analyse_cripto/
    ├── .ipynb_checkpoints/     # Checkpoints automáticos salvos pelo Jupyter Notebook 
    │   └── 02-feature-selection-checkpoint.ipynb 
    ├── api/                             # Diretório com arquivos relacionados à API.
    │   ├── api_server.py                
    │   ├── app.py                       
    │   └── Dockerfile                   
    ├── assets/images/                   # Diretório de imagens usadas no projeto
    │   ├── bitcoin.png        
    │   ├── closedPrice.png              
    │   ├── eos.png                      
    │   ├── matriz.png                   
    │   ├── price.png                    
    │   └── solana.png                   
    ├── data/raw/                        # Diretório para dados brutos de criptomoedas.
    │   ├── coin_Bitcoin.csv             
    │   ├── coin_EOS.csv                 
    │   └── coin_Solana.csv              
    ├── docs/                            # Diretório de documentação do projeto.
    │   ├── docker.md                    # Documentação sobre o uso do Docker.
    │   └── docs.md                      # Documentação geral do projeto.
    │   └── comousar.md                  # Dopcumentação de como rodar a aplicação
    ├── models/                          # Diretório para os modelos de machine learning treinados e scripts relacionados.
    │   ├── model_selection.py           
    │   ├── random_forest_model.pkl      
    │   └── trained-models.pkl           
    ├── notebook/                        # Diretório com notebooks Jupyter
    │   ├── 01-data-exploration.ipynb    
    │   ├── 02-feature-selection.ipynb   
    │   └── 03-dashboard.ipynb           
    ├── .gitignore                       
    └── docker-compose.yml               # Arquivo de configuração do Docker Compose para orquestrar os contêineres da aplicação.
