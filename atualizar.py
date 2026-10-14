import sqlite3

conexao = sqlite3.connect("pizzaria.db")
cursor = conexao.cursor()

codigo = int(input("Digite o código:"))
sabor = input("Digite o sabor: ")
preco = float(input("Preço R$: "))

comando = "UPDATE pizzas SET sabor = ?, preco = ? WHERE codigo = ?"
cursor.execute(comando, (sabor,preco,codigo))



if cursor.rowcount > 0:
    # rowcount serve para informar quantas linhas forma alteradas
    print(f"\nPizza: {sabor} atualizada com sucesso!")
else:
    print("Item não localizado com esse código")
    # valida se existe ou não o código


conexao.commit()
conexao.close()

