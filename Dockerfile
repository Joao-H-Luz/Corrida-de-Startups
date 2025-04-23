# Imagem base com Python 3.13.3-slim
FROM docker-language-server:3.13.3-slim

# Diretório de trabalho
WORKDIR /app

COPY . .

# dependências
RUN pip install --no-cache-dir -r requirements.txt

# Comando para rodar o app
CMD ["python", "app.py"]