import sqlite3

conexao = sqlite3.connect("pizzaria.db")
cursor = conexao.cursor()

codigo = int(input("Digite o código:"))


comando_excluir = "DELETE FROM pizzas WHERE codigo = ?"
cursor.execute(comando_excluir, (codigo,))
# A vírgula cria uma tupla de um único elemento.

if cursor.rowcount > 0:
    print(f"Pizza de código: {codigo}, excluída com sucesso!")
else:
    print("Código não localizado")

conexao.commit()
conexao.close()


