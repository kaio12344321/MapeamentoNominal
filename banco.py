import sqlite3

# Criar o banco de dados SQLite
conexao = sqlite3.connect('clientes.db')

cursor = conexao.cursor()       