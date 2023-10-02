import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# Função para criar o gráfico de barras
def create_line_chart(data):
    fig, ax = plt.subplots()
    ax.plot(data['predicted'], data['accuracy'], marker='o', linestyle='-', color='b')
    ax.set_xlabel('Número de Mortes')
    ax.set_ylabel('Acurácia')
    ax.set_title('Gráfico de Linha - Número de Mortes vs Acurácia')
    st.pyplot(fig)
# Interface Streamlit
def main():
    # Define o título da página com st.title()
    st.title('Previsão de Mortos nas Rodovias do Brasil')
        # Botão para obter dados do backend
    if st.button('Obter Dados do Backend'):

        # URL do endpoint GET do seu backend (substitua com a URL real)
        backend_url = 'http://localhost:8000/model-results'
        
        # Fazer uma chamada GET para o backend
        response = requests.get(backend_url)
        
        if response.status_code == 200:
            # Supondo que o backend retorna os dados em formato JSON
            data = response.json()
            
            # Converter os dados em um DataFrame do Pandas
            df = pd.DataFrame(data)
            
            st.write(df)  # Exibir os dados obtidos do backend
            create_line_chart(df)  # Gerar e exibir o gráfico de barras
        else:
            st.error(f'Erro ao obter dados do backend (Código de Status: {response.status_code})')

if __name__ == "__main__":
    main()
