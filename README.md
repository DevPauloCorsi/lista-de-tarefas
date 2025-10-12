
#  Lista de Tarefas - Fase 

Este é um projeto simples de **Lista de Tarefas ** desenvolvido em **Python (Flask)** com integração ao **MySQL**.
O objetivo é permitir que o usuário cadastre e visualize suas tarefas, organizando suas atividades de forma prática.

---

# Tecnologias Utilizadas

* **Python 3**
* **Flask** (framework web)
* **MySQL** (banco de dados relacional)
* **HTML + CSS** (frontend simples e responsivo)

---

# Estrutura do Projeto

```
lista_de_tarefas/
│-- app.py               # Backend Flask
│-- templates/
│   └── index.html       # Interface principal
│-- static/
│   └── style.css        # Estilos da aplicação
│-- README.md            # Documentação do projeto
```

---

# Banco de Dados

Foi criado o banco de dados **`db_lista_tarefa`** no MySQL, com a tabela:

```sql
CREATE TABLE tarefas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(255) NOT NULL,
    status VARCHAR(50) DEFAULT 'pendente'
);
```

### Colunas:

* `id` → Identificador único da tarefa.
* `descricao` → Texto descritivo da tarefa.
* `status` → Estado da tarefa (**pendente** ou **Concluida**).

---

## Funcionalidades da Fase 1

Adicionar novas tarefas.
Exibir a lista de tarefas cadastradas.
Coluna **status** criada no banco (por padrão aparece como "pendente").
Frontend simples e responsivo.

## Fase 2
A segunda fase trouxe melhorias visuais, funcionais e estruturais no projeto.

Backend (Flask / app.py)
Implementada a rota /concluir/<id> para marcar tarefas como concluídas.
Atualização direta do status no banco de dados.
Validação para evitar salvar tarefas vazias.
Inclusão de cursor.close() e db.commit() após cada operação (boa prática).
Frontend (HTML + CSS)
Adicionado botão verde “Concluir” ao lado de cada tarefa pendente.
Quando o botão é clicado, o status muda para “concluída”.
Tarefas concluídas aparecem com texto riscado e cor cinza.
Layout refeito usando CSS Grid, com 3 colunas fixas:
Descrição | Status | Botão Concluir.


---

## Exemplo de Uso

1.	O usuário digita uma tarefa e clica em **Adicionar**.
2.	A tarefa é salva no banco com o status **pendente**.
3.	A lista exibe a nova tarefa na tela.
4.	Ao clicar em **Concluir**, o status muda para **concluída** e o texto fica riscado.
________________________________________


---

## Como Executar o Projeto

1. Clone o repositório:

```bash
git clone https://github.com/DevPauloCorsi/lista-de-tarefas.git
```

2. Entre na pasta do projeto:

```bash
cd lista-de-tarefas
```

3. Instale as dependências necessárias:

```bash
pip install flask mysql-connector-python
```

4. Configure seu banco de dados MySQL:

* Crie o banco `db_lista_tarefa`
* Execute o script de criação da tabela (mostrado acima).

5. Rode o servidor Flask:

```bash
python app.py
```

6. Acesse no navegador:
    vai aparecer algo como:
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

# Próximos Passos (Fase 3)

* Implementar **botões "aditar e excluir"** para editar ou exluir tarefas e atualizar o status.

---
Projeto desenvolvido para aprendizado e prática integrando **HTML/CSS +Puthon-Flask + Banco MySQL**.


