# Treinos de Jiu-Jitsu

Este é um projeto simples desenvolvido com Django para gerenciar treinos de Jiu-Jitsu. O objetivo do projeto é oferecer uma API para cadastrar, listar e gerenciar treinos, facilitando o acompanhamento dos treinos realizados. Além disso, o sistema permite que os usuários armazenem informações detalhadas sobre cada treino, como data, duração, técnicas praticadas e observações adicionais.

O projeto foi desenvolvido com uma estrutura modular para facilitar futuras expansões, permitindo que novos recursos sejam adicionados conforme necessário. Ele é uma ótima base para quem deseja aprender mais sobre Django e o desenvolvimento de APIs RESTful, utilizando boas práticas de organização e separação de responsabilidades.

## 💻 Tecnologias Utilizadas
- Python 3
- Django
- Django REST Framework
- SQLite (banco de dados padrão, mas pode ser alterado)

## 🚀 Funcionalidades
- Cadastro de treinos com informações detalhadas
- Listagem de treinos com filtros para melhor organização
- API para interação com os treinos através de endpoints REST
- Estrutura modular para facilitar futuras melhorias e expansões
- Banco de dados SQLite como opção padrão, com possibilidade de alteração para outros bancos
- Configuração mínima para rápida instalação e uso

## 📂 Como Executar o Projeto
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/treinos-jiu-jitsu.git
   cd treinos-jiu-jitsu
   ```

2. Crie um ambiente virtual e instale as dependências:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Execute as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```

4. Inicie o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

5. Acesse a aplicação em: `http://127.0.0.1:8000/`

## Estrutura do Projeto
```
mini_projeto_treinos_jiu_jitsu/
│-- core/              # Configurações principais do Django
│-- treino/            # Aplicação para gerenciamento de treinos
│-- manage.py          # Arquivo de gerenciamento do Django
│-- requirements.txt   # Lista de dependências do projeto
```

## ⚠️ Observação
Se estiver utilizando Windows, evite usar o Python 3.13.0, pois pode causar incompatibilidades com algumas bibliotecas do Django.
