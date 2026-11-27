import sqlite3


def conectar_banco():
    # Conecta ao banco de dados SQLite
    conexao = sqlite3.connect('clientes.db')
    return conexao


def limpar_dados_tabela(nome_da_tabela):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    try:
        cursor.execute(f'DELETE FROM "{nome_da_tabela}"')

        cursor.execute("""
            DELETE FROM sqlite_sequence
            WHERE name = ?
        """, (nome_da_tabela,))

        conexao.commit()

    except Exception as erro:
        conexao.rollback()
        print(f"Erro ao limpar tabela: {erro}")

    finally:
        conexao.close()


def insere_dados_xlsx(nome, telefone, endereco):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    dados = list(zip(nome, telefone, endereco))

    try:
        cursor.executemany(
            "INSERT INTO clientes (NOME, TELEFONE, ENDERECO) VALUES (?, ?, ?)",
            dados
        )
        conexao.commit()
    except Exception as e:
        conexao.rollback()
        raise e
    finally:
        cursor.close()
        conexao.close()


def listar_dados():
    conexao = conectar_banco()

    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM clientes")

    # Transformar os resultados em uma lista de tuplas
    resultados = cursor.fetchall()

    cursor.close()
    return resultados
