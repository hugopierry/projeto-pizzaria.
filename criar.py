import sqlite3


conexao = sqlite3.connect("pizzaria.db")
cursor = conexao.cursor()


# novas_colunas = [
#     ("broto","REAL"),
#     ("media","REAL"),
#     ("grande","REAL")
# ]
# for nome, tipo in novas_colunas: 
#     cursor.execute(f"ALTER TABLE pizzas ADD COLUMN {nome} {tipo}")

# df = df.rename(columns={
#     "codigo":"CÓDIGO",
#     "sabor": "SABOR",
#     "broto": "BROTO (R$)",
#     "media": "MÉDIA (R$)",
#     "grande": "GRANDE (R$)"


# })

# alterar_colunas = """
#     ALTER TABLE pizzas RENAME COLUMN grande TO Grande;
# """
# cursor.execute(alterar_colunas)
# conexao.commit()
# print("Colunas editadas com sucesso!")
# conexao.close()







