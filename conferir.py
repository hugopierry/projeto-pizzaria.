import sqlite3


conexao = sqlite3.connect("pizzaria.db")
# concta ao banco

cursor= conexao.cursor()
# cria o cursor

cursor.execute("SELECT * FROM pizzas")

ler_pizzas = cursor.fetchall()
print("PIZZAS E VALORES".center(50))
for ler_pizza in ler_pizzas:
    print(f"Código: {ler_pizza[0]:<2}| Sabor: {ler_pizza [1]:<2} | Valor R$:{ler_pizza [2]:<2}")


conexao.commit()
conexao.close()




