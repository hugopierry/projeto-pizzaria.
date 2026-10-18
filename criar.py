import sqlite3


conexao = sqlite3.connect("pizzaria.db")
cursor = conexao.cursor()


novas_colunas = [
    ("broto","REAL"),
    ("media","REAL"),
    ("grande","REAL")
]
for nome, tipo in novas_colunas: 
    cursor.execute(f"ALTER TABLE pizzas ADD COLUMN {nome} {tipo}")

conexao.commit()
conexao.close()





