import sqlite3

conexao = sqlite3.connect("pizzaria.db")
cursor = conexao.cursor()

print("EXCLUIR PIZZA".center(50))

# Foi adicionado o tratamento de erros: (try e except), para corrigir a inserção de dados 
# incorretos.
try:
    codigo = int(input("\nDigite o código: "))
    comando_excluir = "DELETE FROM pizzas WHERE codigo = ?"
    cursor.execute(comando_excluir, (codigo,))
    if cursor.rowcount > 0:
        print(f"Pizza de código: {codigo}, excluída com sucesso!")
    else:
        print("Código não localizado")
except ValueError:
    print("Erro: digite um número válido.")


conexao.commit()
conexao.close()


