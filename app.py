from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Conexão com MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1735pr40!FR",  
    database="db_lista_tarefa"
)


@app.route('/')
def index():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tarefas")
    tarefas = cursor.fetchall()
    return render_template('index.html', tarefas=tarefas)

@app.route('/add', methods=['POST'])
def add():
    descricao = request.form['descricao']
    cursor = db.cursor()
    cursor.execute("INSERT INTO tarefas (descricao) VALUES (%s)", (descricao,))
    db.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
