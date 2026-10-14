import sqlite3
# Este código cria o banco de dados onde será inserido posteriormente, os dados do banco
# é montado a estrutura do banco de dados
conexao = sqlite3.connect("pizzaria.db")
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS pizzas (
        codigo INTEGER PRIMARY KEY,
        sabor TEXT  NOT NULL,
        preco REAL NOT NULL
    )
""")
# é criado o estilo das colunar para ser informado os dados

cursor.execute(
    "INSERT INTO pizzas (codigo,sabor,preco) VALUES (?,?,?)",
    (3,"Peperone", 45.90)
)


conexao.commit()
conexao.close()

