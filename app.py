# from flask import Flask, render_template, request, redirect
# import mysql.connector

# app = Flask(__name__)

# # Conexão com MySQL
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="1735pr40!FR",  
#     database="db_lista_tarefa"
# )


# @app.route('/')
# def index():
#     cursor = db.cursor(dictionary=True)
#     cursor.execute("SELECT * FROM tarefas")
#     tarefas = cursor.fetchall()
#     return render_template('index.html', tarefas=tarefas)

# @app.route('/add', methods=['POST'])
# def add():
#     descricao = request.form['descricao']
#     cursor = db.cursor()
#     cursor.execute("INSERT INTO tarefas (descricao) VALUES (%s)", (descricao,))
#     db.commit()
#     return redirect('/')

# if __name__ == '__main__':
#     app.run(debug=True)

# Importa as bibliotecas necessárias do Flask e do MySQL
from flask import Flask, render_template, request, redirect
import mysql.connector

# Cria a aplicação Flask
app = Flask(__name__)

# Conexão com o banco de dados MySQL
db = mysql.connector.connect(
    host="localhost",        # Endereço do servidor MySQL
    user="root",             # Usuário do MySQL
    password="1735pr40!FR",  # Senha do MySQL (atenção: cuidado em deixar exposta em código público)
    database="db_lista_tarefa" # Nome do banco de dados
)

# Rota principal do site (página inicial)
@app.route('/')
def index():
    # Cria um cursor que retorna os resultados no formato de dicionário
    cursor = db.cursor(dictionary=True)

    # Busca todas as tarefas na tabela 'tarefas'
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()  # Recupera os resultados

    # Renderiza o template index.html e envia a lista de tarefas para ele
    return render_template('index.html', tarefas=tarefas)


# Rota para adicionar novas tarefas (recebe dados via formulário POST)
@app.route('/add', methods=['POST'])
def add():
    # Pega a descrição da tarefa digitada no formulário
    descricao = request.form['descricao']

    # Cria um cursor normal (sem dicionário)
    cursor = db.cursor()

    # Insere a nova tarefa na tabela
    cursor.execute("INSERT INTO tarefas (descricao) VALUES (%s)", (descricao,))

    # Confirma a inserção no banco (commit salva a operação)
    db.commit()

    # Redireciona de volta para a página inicial
    return redirect('/')


# Garante que a aplicação Flask rode apenas quando o arquivo for executado diretamente
if __name__ == '__main__':
    app.run(debug=True)  # Inicia o servidor em modo debug (mostra erros detalhados)
