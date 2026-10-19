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

# criar_nova_coluna = """
#     ALTER TABLE pizzas ADD Tipo ;
# """
# cursor.execute(criar_nova_coluna)
# conexao.commit()
# print("Colunas adicionada com sucesso!")
# conexao.close()







