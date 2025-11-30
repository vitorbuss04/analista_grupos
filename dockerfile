FROM python:3.10-slim

# Define o diretório de trabalho
WORKDIR /app

# Instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código
COPY . .

# Comando para manter rodando (IMPORTANTE: use -u para logs em tempo real)
CMD ["python", "-u", "main.py"]