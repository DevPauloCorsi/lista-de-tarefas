
#  Lista de Tarefas - Fase 1

Este é um projeto simples de **Lista de Tarefas (To-Do List)** desenvolvido em **Python (Flask)** com integração ao **MySQL**.
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
    status VARCHAR(20) DEFAULT 'pendente'
);
```

### Colunas:

* `id` → Identificador único da tarefa.
* `descricao` → Texto descritivo da tarefa.
* `status` → Estado da tarefa (por padrão: **pendente**).

---

## Funcionalidades da Fase 1

Adicionar novas tarefas.
Exibir a lista de tarefas cadastradas.
Coluna **status** criada no banco (por padrão aparece como "pendente").
Frontend simples e responsivo.

---

## Exemplo de Uso

* O usuário digita uma tarefa no campo de texto.
* A tarefa é salva no banco com o status **pendente**.
* A lista de tarefas é exibida logo abaixo do formulário.

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
   👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

# Próximos Passos (Fase 2)

* Implementar **checkbox/botão "Concluir"** para atualizar o status.
* Exibir tarefas concluídas riscadas na tela.
* Banco de dados: a coluna status continuará presente, agora podendo ter os valores pendente ou concluída.
* Melhorar usabilidade e layout.

---
Projeto desenvolvido para aprendizado e prática de integração **Flask + MySQL**.


