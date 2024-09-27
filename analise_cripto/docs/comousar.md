Para rodar o projeto utilizando Docker, siga os passos abaixo:

# 1. Pré-requisitos

- Tenha o Docker e o Docker Compose instalados no seu sistema.

# 2. Passos para Executar o Projeto

## 2.1 Clonar o Repositório

-------------

    git clone https://github.com/seu-usuario/analise_cripto.git
    cd analise_cripto

-------------

## 2.2 Construir e Subir os Contêineres

No diretório raiz do projeto, onde está localizado o arquivo docker-compose.yml, execute o comando para construir e subir os contêineres:

-----------

    docker-compose up --build

-------------

Este comando irá:

- Construir as imagens para os serviços definidos (API e MySQL).
- Subir os contêineres para o banco de dados MySQL e a API de criptomoedas.

# 3. Verificar o Funcionamento

- O serviço MySQL será iniciado na porta 3306.
- O serviço da API de análise de criptomoedas estará disponível na porta 5000.

Você pode acessar a API na URL: http://localhost:5000.

## 3.1 Verificação do Banco de Dados

Para verificar se o MySQL está rodando corretamente, conecte-se ao contêiner do banco de dados:

-----------
    docker exec -it mysql_db mysql -u root -p

----------

Quando solicitado, use a senha definida no docker-compose.yml.

## 3.2 Logs do Projeto

Pode-se acompanhar os logs dos contêineres em tempo real com o comando:

----------
    docker-compose logs -f
----------

# 4. Encerrar os Contêineres

Para parar e remover os contêineres, use o comando:

--------
    docker-compose down -v
---------

# 5. Possíveis Erros e Soluções

- Erro no MySQL: Se o MySQL não iniciar corretamente, verifique se o volume foi criado com as permissões corretas e se as variáveis de ambiente estão configuradas.
- Arquivo de Modelo Preditivo Faltando: Certifique-se de que o arquivo trained-models.pkl está presente no diretório correto (/models), conforme configurado no projeto.