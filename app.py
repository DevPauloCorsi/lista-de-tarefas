 
from flask import Flask, render_template, request, redirect, url_for, session
# MUDANÇA: agora também é importado "session" para controle de login.
# MUDANÇA: importado url_for para gerar rotas.

import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
# NOVO: funções para gerar hash e validar senhas. 

# Criação do aplicativo Flask
app = Flask(__name__)

# Chave secreta para sessões (necessária para login/logout)
app.secret_key = "chave_super_secreta_aqui"
# NOVO: agora existe controle total de autenticação.

# Conexão com o banco de dados MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1735pr40!FR",
    database="db_lista_tarefa"
)
# Conexão permanece para ambas tabelas tarefa e usuários.
# ROTA DE LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():
    
    # NOVO:  sistema de login novo.
    if request.method == "POST":
        username = request.form["username"]
        senha = request.form["senha"]

        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE username = %s", (username,))
        user = cursor.fetchone()
        cursor.close()

        # NOVO:  senhas — comparação é feita por hash.
        if user and check_password_hash(user["senha"], senha):
            session["usuario_id"] = user["id"]  # NOVO: salvando ID do usuário na sessão
            return redirect(url_for("index"))
        else:
            return render_template("login.html", error="Usuário ou senha inválidos")

    return render_template("login.html")


# ROTA DE CADASTRO
@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    # NOVO: rotA nova — não existia no código antigo.
    if request.method == "POST":
        username = request.form["username"]
        senha = request.form["senha"]

        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE username = %s", (username,))
        if cursor.fetchone():
            return render_template("cadastro.html", error="Usuário já existe")

        # NOVO: senha agora recebe hash
        hash_senha = generate_password_hash(senha)

        cursor.execute("INSERT INTO usuarios (username, senha) VALUES (%s, %s)", 
                       (username, hash_senha))
        db.commit()
        cursor.close()

        # Depois de cadastrar, redireciona ao login
        return redirect(url_for("login"))

    return render_template("cadastro.html")


# ROTA DE LOGOUT
@app.route("/logout")
def logout():
    # NOVO: remove o usuário da sessão
    session.pop("usuario_id", None)
    return redirect(url_for("login"))


# ROTA PRINCIPAL — LISTA TODAS AS TAREFAS
@app.route('/')
def index():
    # MUDANÇA: agora impede acesso de usuários não logados
    if "usuario_id" not in session:
        return redirect(url_for("login"))

    cursor = db.cursor(dictionary=True)

    # NOVO: agora seleciona APENAS tarefas do usuário logado
    cursor.execute("SELECT * FROM tarefas WHERE usuario_id = %s", (session["usuario_id"],))

    tarefas = cursor.fetchall()
    cursor.close()

    return render_template('index.html', tarefas=tarefas)


# ROTA PARA ADICIONAR NOVAS TAREFAS
@app.route('/add', methods=['POST'])
def add():
    # NOVO: só permite adicionar tarefas se estiver logado
    if "usuario_id" not in session:
        return redirect(url_for("login"))

    descricao = request.form['descricao'].strip()

    if descricao:
        cursor = db.cursor()

        # NOVO: agora a tarefa é vinculada ao usuário via usuario_id
        cursor.execute(
            "INSERT INTO tarefas (descricao, status, usuario_id) VALUES (%s, %s, %s)",
            (descricao, 'pendente', session["usuario_id"])
        )

        db.commit()
        cursor.close()

    return redirect('/')


# ROTA PARA CONCLUIR UMA TAREFA
@app.route('/concluir/<int:id>')
def concluir(id):
    # NOVO: agora só conclui tarefas do usuário logado
    if "usuario_id" not in session:
        return redirect(url_for("login"))

    cursor = db.cursor()

    cursor.execute(
        "UPDATE tarefas SET status = 'concluída' WHERE id = %s AND usuario_id = %s",
        (id, session["usuario_id"])
    )

    db.commit()
    cursor.close()
    return redirect('/')


# ROTA PARA EXCLUIR UMA TAREFA
@app.route('/excluir/<int:id>')
def excluir(id):
    # NOVO: exclusão restrita ao proprietário da tarefa
    if "usuario_id" not in session:
        return redirect(url_for("login"))
# NOVO BLOCO adiciona funcionalidade de exclusão
    cursor = db.cursor()
    # Comando SQL DELETE para remover a tarefa do banco
    cursor.execute(
        "DELETE FROM tarefas WHERE id = %s AND usuario_id = %s",
        (id, session["usuario_id"])
    )

    db.commit()
    cursor.close()
    return redirect('/')


# ROTA PARA EDITAR UMA TAREFA
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    # NOVO: edição só pode ser feita por quem está logado
    if "usuario_id" not in session:
        return redirect(url_for("login"))

    cursor = db.cursor(dictionary=True)

    if request.method == 'POST':
        nova_descricao = request.form['descricao'].strip()

        if nova_descricao:
            # NOVO: agora a edição também considera o usuario_id
            cursor.execute("""
                UPDATE tarefas 
                SET descricao = %s, status = 'pendente'
                WHERE id = %s AND usuario_id = %s
            """, (nova_descricao, id, session["usuario_id"]))

            db.commit()

        cursor.close()
        return redirect('/')

    else:
        cursor.execute(
            "SELECT * FROM tarefas WHERE id = %s AND usuario_id = %s",
            (id, session["usuario_id"])
        )

        tarefa = cursor.fetchone()
        cursor.close()
        return render_template('editar.html', tarefa=tarefa)

if __name__ == '__main__':
    app.run(debug=True)
