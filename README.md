# Lista de Tarefas - Fases do Projeto
Este é um projeto simples de **Lista de Tarefas** desenvolvido em **Python (Flask)** com integração ao **MySQL**.
O objetivo é permitir que o usuário cadastre, visualize e organize suas tarefas de forma prática.

# Tecnologias Utilizadas
* **Python 3**
* **Flask** (framework web)
* **MySQL** (banco de dados relacional)
* **HTML + CSS** (frontend simples e responsivo)

# Estrutura do Projeto
lista_de_tarefas/
│-- app.py # Backend Flask
│-- templates/
│ ├── index.html # Lista de tarefas
│ ├── editar.html # Tela de edição
│ ├── login.html # Tela de login
│ └── cadastro.html # Tela de cadastro
│-- static/
│ └── style.css # Estilos gerais
│-- README.md # Documentação do projeto
```
# Banco de Dados

Foi criado o banco de dados **`db_lista_tarefa`** no MySQL, com as tabelas:
```
```db_lista_tarefas_tarefas.sql
CREATE TABLE `tarefas` (
  `id` int NOT NULL AUTO_INCREMENT,
  `descricao` varchar(255) NOT NULL,
  `status` varchar(50) DEFAULT 'pendente',
  `usuario_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_usuario` (`usuario_id`),
  CONSTRAINT `fk_usuario` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE
  ) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```

```db_lista_tarefas_usuario.sql
CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `senha` varchar(255) NOT NULL,
  PRIMARY KEY (`id`), 
  UNIQUE KEY `username` (`username`)
  ) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```

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

## Fase 4 – Login + Lista Personalizada (Entrega Final)
**Autenticação** 
1. Tela de Login (/login).
2. Tela de Cadastro (/cadastro).
3. Verificação de usuário e senha.
4. Sessão ativa com session do Flask.

**Tarefas por usuário**
1. Cada usuário visualiza somente suas tarefas.
2. Todas as rotas agora filtram pelo usuario_id.
3. Ao cadastrar tarefa, é salva vinculada ao usuário logado.

**Segurança**
1. Senhas armazenadas usando hash SHA256 (ou solução mais segura).
2. Sessão protegida com app.secret_key.

## Exemplo de Uso
1. O usuário acessa a página de **Login** e informa seu usuário e senha.
2. Caso ainda não tenha conta, acessa a página de **Cadastro**, cria seu usuário e realiza o login.
3. Após entrar, é redirecionado para sua **lista de tarefas exclusiva**, onde somente suas tarefas são exibidas.
4. Para adicionar uma nova tarefa, o usuário digita o texto no campo apropriado e clica em **Adicionar**.
5. A tarefa é salva no banco de dados vinculada ao **ID do usuário logado**.
6. Na lista, o usuário pode visualizar todas as suas tarefas e realizar ações como:

   * **Concluir**: altera o status para “concluída” e aplica formatação riscada.
   * **Editar**: permite alterar o texto da tarefa; tarefas concluídas voltam ao status “pendente” ao serem editadas.
   * **Excluir**: remove a tarefa definitivamente do banco de dados.
7. Ao terminar, o usuário pode clicar em **Logout** para sair da conta e encerrar a sessão.

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

## Observações
Projeto desenvolvido para fins de estudo, integrando Flask + MySQL + HTML/CSS com autenticação e listas personalizadas de tarefas, finalizado na 4 fase, será posteriormente atualizado para recuperar senha.  