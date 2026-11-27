import sqlite3

# Conexão com o banco de dados SQLite
conexao = sqlite3.connect('clientes.db')

# Envia e recebe dados do banco de dados
cursor = conexao.cursor()

# Criação da tabela "clientes" no banco de dados
cursor.execute(
    """CREATE TABLE IF NOT EXISTS clientes (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOME TEXT NOT NULL,
            TELEFONE TEXT UNIQUE NOT NULL,
            ENDERECO TEXT NOT NULL
        );
    """)

# Fechar a conexão com o banco de dados (Economiza recursos e evita problemas de concorrência)
cursor.close()

print("Tabela 'clientes' criada com sucesso no banco de dados 'clientes.db'.")
