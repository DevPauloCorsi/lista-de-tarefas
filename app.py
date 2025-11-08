# IMPORTAÇÕES E CONFIGURAÇÃO DO APP
from flask import Flask, render_template, request, redirect
import mysql.connector

# Criação do aplicativo Flask
app = Flask(__name__)

# Conexão com o banco de dados MySQL — permanece igual
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1735pr40!FR",
    database="db_lista_tarefa"
)

# ROTA PRINCIPAL — LISTA TODAS AS TAREFAS
@app.route('/')
def index():
    # Mantido: usa cursor como dicionário para acessar por nome de coluna
    cursor = db.cursor(dictionary=True)

    # Já havia sido alterado antes para incluir o campo "status" no SELECT
    cursor.execute("SELECT * FROM tarefas")

    tarefas = cursor.fetchall()
    cursor.close()  # Boa prática adicionada em versões anteriores

    # Exibe agora as tarefas com status (pendente / concluída)
    return render_template('index.html', tarefas=tarefas)

# ROTA PARA ADICIONAR NOVAS TAREFAS
@app.route('/add', methods=['POST'])
def add():
    # strip() remove espaços extras — melhoria adicionada
    descricao = request.form['descricao'].strip()

    # Previne salvar tarefas em branco
    if descricao:
        cursor = db.cursor()

        # ALTERAÇÃO: agora o INSERT também inclui o campo "status"
        # Todas as tarefas novas começam como 'pendente'
        cursor.execute(
            "INSERT INTO tarefas (descricao, status) VALUES (%s, %s)",
            (descricao, 'pendente')
        )

        db.commit()  
        cursor.close()  # Fechamento do cursor — adicionado como boa prática

    return redirect('/')

# CONCLUIR UMA TAREFA — já existia
@app.route('/concluir/<int:id>')
def concluir(id):
    cursor = db.cursor()

    # Atualiza o campo status para "concluída"
    cursor.execute("UPDATE tarefas SET status = 'concluída' WHERE id = %s", (id,))

    db.commit()
    cursor.close()
    return redirect('/')

# NOVA ROTA: EXCLUIR UMA TAREFA
@app.route('/excluir/<int:id>')
def excluir(id):
    # NOVO BLOCO adiciona funcionalidade de exclusão
    cursor = db.cursor()

    # Comando SQL DELETE para remover a tarefa do banco
    cursor.execute("DELETE FROM tarefas WHERE id = %s", (id,))

    db.commit()   # Aplica a exclusão permanentemente
    cursor.close()
    return redirect('/')

# NOVA ROTA: EDITAR UMA TAREFA
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    # Usa dictionary=True para acessar colunas por nome
    cursor = db.cursor(dictionary=True)
    
    # Quando o formulário for enviado (POST):
    if request.method == 'POST':
        nova_descricao = request.form['descricao'].strip()
        if nova_descricao:
            # Atualiza a descrição e redefine o status para "pendente"
            #  (mesmo se ela já estava concluída)
            cursor.execute("""
                UPDATE tarefas 
                SET descricao = %s, status = 'pendente'
                WHERE id = %s
            """, (nova_descricao, id))
            db.commit()
        
        cursor.close()
        return redirect('/')
    
    # Quando a rota for acessada via GET (abrindo a página de edição)
    else:
        # Busca os dados da tarefa para preencher o campo no formulário
        cursor.execute("SELECT * FROM tarefas WHERE id = %s", (id,))
        tarefa = cursor.fetchone()
        cursor.close()
        
        # Renderiza o novo template "editar.html"
        return render_template('editar.html', tarefa=tarefa)

# EXECUÇÃO DO SERVIDOR FLASK
if __name__ == '__main__':
    app.run(debug=True)
