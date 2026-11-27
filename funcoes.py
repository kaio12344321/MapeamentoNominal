import sqlite3

def conectar_banco():
    # Conecta ao banco de dados SQLite
    conexao = sqlite3.connect('clientes.db')
    return conexao

def insere_dados(nome, telefone, endereco):
    conexao = conectar_banco()

    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO clientes (NOME, TELEFONE, ENDERECO) VALUES (?, ?, ?)",
        (nome, telefone, endereco)
    )

    # Salvar as alterações no banco de dados
    conexao.commit()
    cursor.close() 


def listar_dados():
    conexao = conectar_banco()

    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes")
    
    # Transformar os resultados em uma lista de tuplas
    resultados = cursor.fetchall()

    cursor.close()
    return resultados

