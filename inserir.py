import sqlite3

conexao = sqlite3.connect("pizzaria.db")
cursor = conexao.cursor()


codigo = int(input("Digite o código:"))
sabor = input("Digite o sabor: ")
preco = float(input("Preço R$: "))

comando_inserir = "INSERT INTO pizzas (codigo, sabor, preco) VALUES (?,?,?)"
cursor.execute(comando_inserir, (codigo,sabor,preco))

conexao.commit()
print(f"Pizza inserida com sucesso!")
conexao.close()


