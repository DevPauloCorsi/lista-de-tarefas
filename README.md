Lista de Tarefas – Fase 1
Descrição do Projeto

Aplicativo web simples para gerenciamento de tarefas.
O usuário pode adicionar tarefas e visualizar a lista. Todas aparecem como "pendentes" no front-end.

Funcionalidades
Adicionar tarefas via formulário.
Visualizar tarefas cadastradas.
Front-end responsivo, simples.

Tecnologias Utilizadas
Backend: Python + Flask
Banco de Dados: MySQL (colunas id, descricao e status)
Frontend: HTML + CSS

| Coluna    | Tipo         | Descrição                             |
| --------- | ------------ | ------------------------------------- |
| id        | INT          | Chave primária, auto-incremento       |
| descricao | VARCHAR(255) | Texto da tarefa                       |
| status    | VARCHAR(20)  | Status da tarefa (pendente)           |


Executando o Projeto

Clonar o repositório:

git clone https://github.com/DevPauloCorsi/lista-de-tarefas.git


Instalar dependências:

pip install flask mysql-connector-python


Configurar o banco de dados MySQL:

Criar a base db_lista_tarefa

Criar a tabela tarefas com as colunas id, descricao e status

Rodar o aplicativo:

python app.py


Abrir o navegador em http://127.0.0.1:5000

Estrutura de Arquivos
lista-de-tarefas/
│
├─ app.py          # Arquivo principal do Flask
├─ templates/
│   └─ index.html  # Página principal
├─ static/
│   └─ style.css   # Estilos do projeto
└─ README.md       # Este arquivo.