# Use a imagem base do Python
FROM python:3.8-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie o seu código, requirements.txt e o modelo para o contêiner
COPY main.py .
COPY requirements.txt .
COPY api_ponderada_teste.pkl .
COPY modelo_ponderada3_teste.pkl .
# Instale as dependências Python especificadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exponha a porta em que a aplicação estará ouvindo
EXPOSE 3000

# Execute a sua aplicação FastAPI
CMD ["uvicorn", "minha_api:app", "--host", "0.0.0.0", "--port", "3000"]