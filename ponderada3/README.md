<img src="../static/logo-inteli.png" alt="Logo do Inteli" style="height: 100%; width:50vp; display: block; margin-left: auto; margin-right: auto; margin-bottom:16px"/>

# Atividade 3: Deploy de modelo de Machine Learning na Nuvem

## Enunciado

Construção e deploy de um modelo de predição ou classificação criados pelos alunos. Este modelo deve ser deployado em uma nuvem comercial e uma API de acesso a ele deve ser desenvolvida.

> ***IMPORTANTE 1:*** Para está entrega, não é necessário construir uma interface de usuário para o modelo, como um frontend. Apenas a API de acesso ao modelo deve ser desenvolvida. 

***IMPORTANTE 2:*** Para está entrega, dois pontos são obrigatórios: 

1. A utilização do Python com o FastAPI para realizar a construção da API;
2. O deploy com o imagens de containers no DockerHub.

O estudante deve escolher um conjunto de dados dentre os relacionados abaixo. Qualquer conjunto diferente destes deve ser aprovado pelo professor. Toda a manipulação realizada com os dados deve ser descrita na documentação do projeto.

O conjunto de dados escolhido deve ser utilizado para a construção de um modelo de predição ou classificação. O modelo deve ser construído utilizando o Python e o framework de Machine Learning de preferência do estudante. A escolha do modelo deve ser justificada pelo estudante.

O ambiente de desenvolvimento deve ser documentado, assim como o ambiente de produção. Um video deve ser gravado apresentado o processo de utilização do modelo em produção.

> ***IMPORTANTE:*** Depois de gravado o comportamento do projeto em produção, o estudante deve remover os recursos alocados na nuvem comercial. Apenas o vídeo será utilizado para a avaliação do projeto, em conjunto com os códigos fontes desenvolvidos.

## Solução

### 1. Escolha do Conjunto de Dados
O conjunto de dados escolhidos para o tratamento e criação do modelo de predição foi - [Brazil: Total highway crashes 2010 - 2023](https://www.kaggle.com/datasets/liamarguedas/brazil-total-highway-crashes-2010-2023).

### 2. Tratamento dos dados e criação do modelo
O tratamento dos dados foi feito em dois arquivos, ambos com extensão em Jupyter Notebook, o primeiro arquivo 'Ponderada3.ipynb' possui o tratamento dos dados brutos retirado direto do link do conjunto de dados, sem a geração do modelo com o PyCaret, e o segundo 'Ponderada3-Colab.ipynb' possui a normalização e padronização a partir do conjunto de dados tratado no arquivo anterior, além da geração do modelo com o PyCaret e geração da API, assim como a geração do arquivo '.pkl' com o modelo serialziado para a utilização da API.

O Modelo gerado tenta predizer a quantidade de mortes em acidentes no trânsito no Brasil.

### 3. Desenvolvimento da API
A API gerada pelo PyCarte foi feita em FastAPI, e nela tem-se a criação de uma rota do tipo 'post' em que os dados são inputados de acordo com as variáveis presentes no dataset, e dessa forma retorna a probabilidade de quantidade de mortos de acordo com os dados de trânsito inputados.

Para rodar a api é necessário executar o comando:
<pre><code>
uvicorn main:app
</code></pre>

### 4. Dockerização
Um aruqivo docker foi gerado para que seja possível a execução da API conteinerizada. Para que seja possível usar o contêiner, é necessário baixar a imagem por meio do comando:
<pre><code>
docker pull jeanrothstein/ponderada3:latest
</code></pre>

e depois:
<pre><code>
docker run -p 3000:3000 ponderada3
</code></pre>

### 5. Comentários finais
Por algum motivo a API não está rodando por conta de um erro em que é dito que o setup do modelo não é feito, sendo que ele é feito:
<pre><code>
ValueError: _CURRENT_EXPERIMENT global variable is not set. Please run setup() first.
</code></pre>

