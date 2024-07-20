# Employee Management API RESTful

   API RESTful para gerenciar cadastros de funcionários com funcionalidades de listagem, criação e edição.

## Configuração e Execução 

### Pré - requisitos

- Python 3.9+
- PostgreSQL

### Instalação:

 1. Repositório GIT:
   Clone o repositório
   ```sh
    git clone https://github.com/thamissena/BackEnd_Employee
    cd BackEnd_Employee
    ```
   
 2. Crie e ative o ambriente virtual e ative-o:
      ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use: venv\Scripts\activate
    ```

 3. Intale as dependêmcias:
   ```sh
    pip install -r requirements.txt
    ```

 4. Inicializar o banco de dados: 
   Crie um banco de dados PostgreSQL e um usuário com permissões adequadas. Atualize a string de conexão no arquivo `run.py` conforme necessário:

    ```python
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://<usuario>:<senha>@localhost/<nome_do_banco>"
    ```

 5. Execute a aplicação: 
    python run.py

6. Acesse a API:
    A API estará disponível em `http://127.0.0.1:5000`.

