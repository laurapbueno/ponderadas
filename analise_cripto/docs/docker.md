# Dockerização para Microsserviço de Análise de Criptomoedas

# 1. Descrição do projeto

Este projeto tem como objetivo criar um microsserviço para análise de criptomoedas. A dockerização permite encapsular a aplicação e seus componentes em contêineres, garantindo portabilidade, facilidade de replicação, e gerenciamento eficiente de dependências. A infraestrutura usa Docker e Docker Compose para gerenciar a aplicação e uma instância MySQL para persistência de dados. O microsserviço fornece uma API para análise de dados históricos de criptomoedas e predições baseadas em um modelo treinado.

# 2. Justificativa de escolha

A escolha de um Microsserviço de Análise de Criptomoedas se deu pela necessidade de encapsular uma solução que interage com um banco de dados, aplica um modelo de machine learning para predição de preços e oferece uma API simples para consultas externas. A abordagem modular e escalável dos microsserviços permite que cada componente (API, banco de dados, e modelo preditivo) funcione de maneira isolada, facilitando a manutenção e o desenvolvimento.

# 3. Arquivos de Deployment

## 3.1 Dockerfile

O Dockerfile define o ambiente para o microsserviço, instalando as dependências do Python e configurando o diretório de trabalho para a API.

-----------

    # Usando uma imagem base do Python
    FROM python:3.9-slim

    # Definir o diretório de trabalho dentro do container
    WORKDIR /app

    # Copiar o arquivo de requisitos para dentro do container
    COPY ./requirements.txt /app/requirements.txt

    # Instalar as dependências do projeto
    RUN pip install --upgrade pip
    RUN pip install -r requirements.txt

    # Copiar o código da aplicação para o diretório /app
    COPY ./api /app

    # Comando de inicialização do servidor da API
    CMD ["python", "api_server.py"]

------------------

## 3.2 docker-compose.yml

O docker-compose.yml define dois serviços: um banco de dados MySQL para persistência de dados e a API Python que processa e disponibiliza as análises de criptomoedas.

------------------------

    version: '3.8'

    services:
    # Serviço do banco de dados MySQL
    db:
        image: mysql:5.7
        container_name: mysql_db
        environment:
        MYSQL_ROOT_PASSWORD: example
        MYSQL_DATABASE: crypto_db
        MYSQL_USER: root
        MYSQL_PASSWORD: example
        ports:
        - "3306:3306"
        volumes:
        - db_data:/var/lib/mysql
        networks:
        - crypto_net

    # Serviço da API de criptomoedas
    api:
        build: ./api
        container_name: crypto_api
        ports:
        - "5000:5000"
        depends_on:
        - db
        networks:
        - crypto_net

    volumes:
    db_data:

    networks:
    crypto_net:

---------------------------

## 3.3 Estrutura de Pastas

-----------------------

    .
    ├── api
    │   ├── app.py
    │   ├── api_server.py
    │   └── models
    │       └── trained-models.pkl
    ├── docker-compose.yml
    ├── Dockerfile
    └── requirements.txt

-------------------------

- app.py e api_server.py: Contêm o código da API que faz o processamento e a consulta de dados.
- models/trained-models.pkl: Modelo treinado utilizado para realizar predições.
- requirements.txt: Lista de dependências Python que são instaladas no contêiner.

# 4. Justificativa da Escolha das Tecnologias

- Python foi escolhido pela facilidade de desenvolvimento de APIs com frameworks leves como Flask ou FastAPI e sua compatibilidade com bibliotecas populares de machine learning, como scikit-learn e joblib.
- MySQL foi escolhido para o banco de dados devido à sua confiabilidade e simplicidade de integração com microsserviços.
- Docker e Docker Compose foram escolhidos para permitir o desenvolvimento isolado em contêineres, além de facilitar a replicação do ambiente de desenvolvimento e produção.