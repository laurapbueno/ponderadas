# ./api/Dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copiar os arquivos de requisitos
COPY requirements.txt /app/requirements.txt

# Copiar os arquivos do projeto
COPY app.py /app/app.py
COPY api_server.py /app/api_server.py

# Atualizar pip e instalar as dependências
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Comando para iniciar a aplicação
CMD ["python", "api_server.py"]
