# IMPORTAÇÕES E CONFIGURAÇÃO DO APP
from flask import Flask, render_template, request, redirect
import mysql.connector

# Criação do aplicativo Flask
app = Flask(__name__)

# Conexão com o banco de dados MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1735pr40!FR",
    database="db_lista_tarefa"
)


# ROTA PRINCIPAL — LISTA TODAS AS TAREFAS
@app.route('/')
def index():
    # Isso faz com que o resultado venha como dicionário (acessamos por nome da coluna)
    cursor = db.cursor(dictionary=True)

    # alterado para incluir a coluna "status"
    cursor.execute("SELECT * FROM tarefas")

    # Recupera todas as tarefas
    tarefas = cursor.fetchall()

    cursor.close()  # Boa prática: fecha o cursor após usar

    # Renderiza o template com a lista de tarefas e seus status
    return render_template('index.html', tarefas=tarefas)



# ROTA PARA ADICIONAR NOVAS TAREFAS
@app.route('/add', methods=['POST'])
def add():
    # NOVO: strip() remove espaços extras no início/fim
    descricao = request.form['descricao'].strip()

    # Evita salvar tarefas vazias
    if descricao:
        cursor = db.cursor()

        # ALTERADO: agora o INSERT inclui também o campo 'status'
        # Todas as novas tarefas começam com status 'pendente'
        cursor.execute(
            "INSERT INTO tarefas (descricao, status) VALUES (%s, %s)",
            (descricao, 'pendente')
        )

        db.commit()  # Confirma a inserção
        cursor.close()  # Fecha o cursor incluido na fase 2

    # Retorna para a página inicial
    return redirect('/')


# NOVA ROTA fase 2: CONCLUIR UMA TAREFA
# permite atualizar o status da tarefa de 'pendente' → 'concluída'
@app.route('/concluir/<int:id>')
def concluir(id):
    cursor = db.cursor()

    #  Atualiza o campo 'status' da tarefa no banco de dados
    cursor.execute("UPDATE tarefas SET status = 'concluída' WHERE id = %s", (id,))

    db.commit()  # Grava a atualização
    cursor.close()  # Fecha o cursor

    # Retorna para a página principal (onde o status agora aparece atualizado)
    return redirect('/')


# EXECUÇÃO DO SERVIDOR FLASK
if __name__ == '__main__':
    app.run(debug=True)
