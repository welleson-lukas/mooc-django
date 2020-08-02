# Bem vindo ao Projeto Curso MOOC do PRODAP

Este projeto foi construído em Django.

## Funcionamento

Clone o projeto, e rode:

    pip install -r requirements.txt

Em seguida, rode na sequência:

    python manage.py migrate
    python manage.py createsuperuser # vai criar o superusuário, siga as intruções

Se todos os comandos funcionarem corretamente, rode o servidor:

    python manage.py runserver

Acesse o painel administrativo em: http://localhost:8000/admin


## Desafio

- Finalizar o módulo de questões;
- Adicionar de forma automática o usuário autenticado, sem precisar setar manualmente;
- Adicionar pesquisa por titulo e filtros por categorias e data em Posts;
- Adicionar pesquisa por titulo e filtros por categorias e data em Topicos;
- Adicionar filtros por data em Respostas;
- Adicionar pesquisa por titulo e filtros por Categorias e Data em Questões;
- Adicionar pesquisa por titulo e filtros por Data em Categorias e Tags;
- Dockerizar no projeto;
- Opcional: Melhorar o visual do Admin Dashboard;

## Link para o vídeo

- https://drive.google.com/file/d/129CD6jzzLE7qXYjUxvmdZOqLkGdWOhLt/view?usp=sharing