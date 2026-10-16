import sqlite3

conexao = sqlite3.connect("pizzaria.db")
cursor = conexao.cursor()

resposta = "S"

# Laço de repetição (While) criado para controlar o fluxo do sistema.
while resposta !="N":

    print("INSERIR PIZZA: " .center(50))
    codigo = int(input("\nDigite o código: "))
    sabor = input("Digite o sabor: ")
    preco = float(input("Preço R$: "))
    resposta = input("Continuar? : [S/N] ").strip().upper()
    print(f"Pizza inserida com sucesso!")

    comando_inserir = "INSERT INTO pizzas (codigo, sabor, preco) VALUES (?,?,?)"
    cursor.execute(comando_inserir, (codigo,sabor,preco))

conexao.commit()

conexao.close()


