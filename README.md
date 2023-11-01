OpenAI FAQ Generator with Flask
Descrição
Este projeto consiste em um gerador de respostas para Perguntas Frequentes (FAQ), utilizando o framework Flask para o back-end e a API do ChatGPT da OpenAI para a geração de texto. O objetivo é criar um serviço simples mas poderoso que pode gerar respostas para perguntas comuns em um determinado campo.

Estrutura de Diretórios
lua
Copy code
/faq_gpt
|-- /templates
|   |-- index.html
|-- /static
|   |-- /css
|       |-- main.css
|-- app.py
|-- requirements.txt
|-- README.md
Componentes
/templates
Este diretório contém os arquivos HTML que definem a interface do usuário. No nosso caso, um único arquivo index.html é suficiente para fornecer a interface de usuário necessária.

/static/css
Este diretório armazena as folhas de estilo CSS que são usadas para estilizar a página HTML.

app.py
Este é o arquivo principal do projeto e contém toda a lógica de back-end. Ele é responsável por iniciar o servidor Flask, bem como por manipular as requisições e respostas HTTP.

requirements.txt
Lista todas as bibliotecas Python necessárias para executar o projeto. As principais dependências são Flask e a biblioteca requests para chamadas HTTP.

Fluxo de Operações
Interface do Usuário: O usuário acessa a página index.html e insere uma pergunta no formulário disponível.
Rota do Flask: Uma rota específica no app.py é acionada quando o formulário é submetido.
API da OpenAI: A pergunta é enviada para a API da OpenAI através de uma chamada HTTP.
Processamento de Resposta: A resposta da API é processada e formatada no app.py.
Exibição de Resposta: A resposta é então exibida ao usuário na página web.
Tecnologias Utilizadas
Back-end: Flask
Front-end: HTML/CSS
Chamadas HTTP: Biblioteca requests



