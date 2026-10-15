import sqlite3


conexao = sqlite3.connect("pizzaria.db")
cursor = conexao.cursor()

# Cria a tabela "pizzas" apenas se ela ainda não existir.
# Se já existir, o SQLite ignora o comando (IF NOT EXISTS) e segue sem dar erro,
# então o script pode rodar mais de uma vez.
# no caso se existir, pode rodar e o banco não recebe nenhuma alteração.
cursor.execute("""
    CREATE TABLE IF NOT EXISTS pizzas (
        codigo INTEGER PRIMARY KEY,
        sabor TEXT  NOT NULL,
        preco REAL NOT NULL
    )
""")

conexao.commit()
conexao.close()





