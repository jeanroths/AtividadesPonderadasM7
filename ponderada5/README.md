<img src="../static/logo-inteli.png" alt="Logo do Inteli" style="height: 100%; width:50vp; display: block; margin-left: auto; margin-right: auto; margin-bottom:16px"/>

# Atividade 5: Resenha sobre o artigo

## Enunciado

Esta atividade ponderada tem por objetivo realizar a construção de uma comparação com o que foi desenvolvido nas outras atividades ponderadas e o artigo lido durante o autoestudo da semana. Os alunos deverão fazer uma comparação do que foi implementado por eles, com o que foi proposto pelo artigo, comparando as similaridades e diferenças. A resenha não deve possuir mais que 1000 palavras, sendo que, eventuais códigos utilizados para demonstração, não fazem parte desta contagem.

Artigo de referência: [Machine learning for internet of things data analysis: a survey](https://www.sciencedirect.com/science/article/pii/S235286481730247X)

## Padrão de qualidade

Os pontos que serão avaliados na entrega do projeto:
1. ***(Até 4.0 ponto)*** Sumarização dos pontos principais do artigo: apresentou uma sumarização com as informações principais do artigo;
2. ***(Até 3.0 ponto)*** Comparação com as técnicas utilizadas no desenvolvimento do projeto;
3. ***(Até 3.0 ponto)*** Resenha Crítica: desenvolvimento de uma resenha crítica sobre o artigo, apresentando os pontos positivos e negativos, destacando o que foi testado no projeto.


# Análise do artigo "Machine learning for internet of things data analysis: a survey" e comparação com o projeto de manutenção preditiva dos sistemas de sangria das aeronaves da Azul

Nome: Jean Lucas Rothstein Machado

Turma: Engenharia da Computação 2022.1

## Sumarização dos pontos principais do artigo:

### 1.Introdução:
A introdução do artigo apresenta o contexto do Internet of Things (IoT) e destaca a importância da análise de dados nesse cenário. Ela estabelece a base para a discussão sobre o uso de aprendizado de máquina no IoT.

### 2.Revisão da Literatura:
A seção de revisão da literatura fornece uma visão geral das pesquisas anteriores relacionadas ao uso de aprendizado de máquina no contexto do IoT. Isso inclui uma análise das tendências e desafios identificados por outros pesquisadores.

### 3.IoT:
O artigo explora o conceito do Internet of Things (IoT) em detalhes. Isso envolve a descrição de como os dispositivos estão interconectados e como eles geram uma grande quantidade de dados que podem ser analisados para obter informações valiosas.

### 4.Smart City:
Dentro do contexto do IoT, o artigo também discute a aplicação desses conceitos em "cidades inteligentes" (Smart Cities). Isso envolve a utilização de sensores e dispositivos para melhorar a eficiência e qualidade de vida nas cidades.

### 5.Taxonomia de Algoritmos de Aprendizado de Máquina:
Uma parte importante do artigo é a criação de uma taxonomia de algoritmos de aprendizado de máquina. Isso implica a categorização dos algoritmos em diferentes classes, como aprendizado supervisionado e não supervisionado, e a descrição de suas aplicações no IoT.

### 6.Discussão da Taxonomia de Algoritmos de Aprendizado de Máquina:
O artigo discute em detalhes a taxonomia criada, explicando como cada classe de algoritmo pode ser aplicada de forma benéfica na análise de dados do IoT. Isso fornece uma compreensão mais profunda das técnicas disponíveis.

### 7.Tendências de Pesquisa e Questões em Aberto:
A seção de tendências de pesquisa e questões em aberto destaca os desafios atuais e futuros no campo do aprendizado de máquina no IoT. Isso inclui a privacidade dos dados, a segurança e a escalabilidade.

### 8.Conclusões:
As conclusões do artigo resumem os principais pontos discutidos, destacando a importância do aprendizado de máquina no IoT. Também pode sugerir possíveis direções para futuras pesquisas e desenvolvimentos na área

## Comparação com técnicas utilizadas no projeto:
No projeto da Azul, foram aplicadas técnicas de regressão e classificação para desenvolver modelos de manutenção preditiva. Esses modelos foram gerados com o auxílio da biblioteca PyCaret, que automatiza o processo de seleção e treinamento de algoritmos de machine learning. Esse aspecto se alinha com o que foi discutido no artigo, que também abordou o uso de algoritmos de classificação e regressão, embora sem foco específico em projetos de manutenção preditiva.

Um ponto notável no projeto da Azul é o uso da computação em nuvem, com ênfase na AWS (Amazon Web Services). A AWS foi utilizada para hospedar tanto o modelo de machine learning quanto a aplicação web associada ao modelo. Isso ressalta a importância da computação em nuvem para garantir escalabilidade e disponibilidade em projetos desse tipo. O artigo menciona a relevância da computação em nuvem no contexto do IoT para lidar com grandes volumes de dados, embora não entre em detalhes sobre a infraestrutura específica da AWS.

Além disso, no projeto da Azul, houve o tratamento de dados de séries temporais e dados sequenciais, o que é comum em projetos de manutenção preditiva. Essa análise envolveu a detecção de padrões ao longo do tempo para prever falhas nas turbinas das aeronaves. Embora o artigo não aborde explicitamente o uso de séries temporais, ele discute o processamento geral de dados do IoT, o que sugere que a análise de séries temporais é relevante para muitos casos de uso do IoT, mesmo que não seja detalhada no texto.

Em resumo, no projeto da Azul técnicas de regressão e classificação com o auxílio do PyCaret foram aplicadas, e foi feito o uso da AWS para hospedar modelos e aplicativos web, o que envolveu a análise de séries temporais e dados sequenciais para prever falhas nas turbinas. A combinação das práticas do projeto e dos conceitos gerais do artigo são importantes para a compreensão e aplicação prática no campo da manutenção preditiva.

## Resenha Crítica

O artigo "Machine learning for internet of things data analysis: a survey" oferece uma análise abrangente das aplicações de aprendizado de máquina no contexto do Internet of Things (IoT). O texto inicia destacando a crescente relevância do IoT na coleta de dados em grande escala e a importância da computação em nuvem para lidar com esses volumes massivos de informações. Em seguida, o artigo revisa várias técnicas de aprendizado de máquina, categorizando-as em diferentes classes, como aprendizado supervisionado e não supervisionado.

Uma das principais forças do artigo reside na sua capacidade de fornecer uma visão geral ampla e acessível das técnicas de aprendizado de máquina aplicadas ao IoT. Ele oferece uma introdução sólida ao assunto, tornando-o acessível a uma ampla audiência, desde iniciantes até especialistas. Além disso, o texto destaca os desafios críticos enfrentados ao lidar com dados do IoT, como questões de privacidade e segurança, e oferece informações sobre ferramentas e plataformas disponíveis para implementação prática.

No entanto, algumas áreas de aprimoramento podem ser consideradas. Primeiramente, embora o artigo forneça uma visão geral útil das técnicas de aprendizado de máquina, ele carece de exemplos práticos e casos de uso específicos, o que poderia ter enriquecido o conteúdo e fornecido aos leitores uma compreensão mais profunda da aplicação dessas técnicas no mundo real.

Além disso, outro aspecto a ser considerado é a falta de detalhes técnicos específicos, como a implementação prática dos serviços de nuvem, incluindo a AWS, que são vitais para projetos de IoT. Embora o artigo reconheça a relevância da computação em nuvem, ele não fornece informações detalhadas sobre como os serviços de nuvem podem ser usados em projetos reais.

Em resumo, o artigo "Machine learning for internet of things data analysis: a survey" é uma leitura valiosa para quem deseja obter uma visão geral das aplicações de aprendizado de máquina no IoT. Ele é acessível e informativo, embora possa ser aprimorado com exemplos práticos e informações atualizadas. A combinação desse conhecimento geral com a experiência prática em projetos, como o desenvolvido pela Azul, pode ser altamente benéfica para profissionais que buscam aplicar esses conceitos no mundo real.