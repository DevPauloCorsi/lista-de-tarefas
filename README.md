# Lista de Tarefas - Fases do Projeto

Este é um projeto simples de **Lista de Tarefas** desenvolvido em **Python (Flask)** com integração ao **MySQL**.
O objetivo é permitir que o usuário cadastre, visualize e organize suas tarefas de forma prática.

---

# Tecnologias Utilizadas

* **Python 3**
* **Flask** (framework web)
* **MySQL** (banco de dados relacional)
* **HTML + CSS** (frontend simples e responsivo)



# Estrutura do Projeto

lista_de_tarefas/
│-- app.py               # Backend Flask
│-- templates/
│   ├── index.html       # Interface principal
│   └── editar.html      # Tela para editar tarefas (Fase 3)
│-- static/
│   └── style.css        # Estilos da aplicação
│-- README.md            # Documentação do projeto
```
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
* `status` → Estado da tarefa (**pendente** ou **concluída**).

## Funcionalidades da Fase 1

* Adicionar novas tarefas.
* Exibir a lista de tarefas cadastradas.
* Coluna **status** criada no banco (por padrão aparece como "pendente").
* Frontend simples e responsivo.

## Fase 2

**Backend (Flask / app.py)**

* Implementada a rota `/concluir/<id>` para marcar tarefas como concluídas.
* Atualização direta do status no banco de dados.
* Validação para evitar salvar tarefas vazias.
* Inclusão de `cursor.close()` e `db.commit()` após cada operação (boa prática).

**Frontend (HTML + CSS)**

* Adicionado botão verde **“Concluir”** ao lado de cada tarefa pendente.
* Quando clicado, o status muda para **concluída**.
* Tarefas concluídas aparecem com texto riscado e cor cinza.
* Layout refeito usando **CSS Flexbox**, com três áreas principais:

  1. Descrição da tarefa
  2. Status
  3. Botões de ação

## Fase 3

**Backend (Flask / app.py)**

* Implementadas rotas `/editar/<id>` e `/excluir/<id>`.
* Ao editar uma tarefa:

  * O texto pode ser alterado.
  * Se a tarefa estava **concluída**, ela volta para **pendente** automaticamente.
  * O botão **Concluir** reaparece.
* Ao excluir uma tarefa, ela é removida do banco de dados.

**Frontend (HTML + CSS)**

* Adicionados **botões “Editar” e “Excluir”** ao lado de cada tarefa.
* Botões alinhados à direita, mantendo o layout organizado.
* Status **pendente** aparece em **amarelo**; **concluída** em **verde**.
* Tooltip mostra o texto completo da tarefa caso ele seja truncado pelo limite de caracteres.

## Exemplo de Uso

1. O usuário digita uma tarefa e clica em **Adicionar**.
2. A tarefa é salva no banco com o status **pendente**.
3. A lista exibe a nova tarefa na tela.
4. Ao clicar em **Concluir**, o status muda para **concluída** e o texto fica riscado.
5. Ao clicar em **Editar**, a tarefa pode ser alterada e volta para **pendente** se já estava concluída.
6. Ao clicar em **Excluir**, a tarefa é removida da lista e do banco de dados.

## Como Executar o Projeto

1. Clone o repositório:

```bash
git clone https://github.com/DevPauloCorsi/lista-de-tarefas.git
```

2. Entre na pasta do projeto:

```bash
cd lista-de-tarefas
```

3. Instale as dependências:

```bash
pip install flask mysql-connector-python
```

4. Configure seu banco de dados MySQL:

* Crie o banco `db_lista_tarefa`.
* Execute o script de criação da tabela (mostrado acima).

5. Rode o servidor Flask:

```bash
python app.py
```

6. Acesse no navegador:

[http://127.0.0.1:5000](http://127.0.0.1:5000)

## Fase 4 (Planejada)

* Criar tela de **Login/Cadastro** (usuário e senha).
* Cada usuário só vê **suas próprias tarefas**.
* Atualizações no banco de dados:

  * Criar tabela **usuarios**.
  * Relacionar tabela **tarefas** → cada tarefa pertence a um usuário.

## Observações
Projeto desenvolvido para aprendizado e prática integrando **HTML/CSS + Python-Flask + Banco MySQL**.