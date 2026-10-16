import sqlite3


conexao = sqlite3.connect("pizzaria.db")
cursor = conexao.cursor()
print("-"*60)
print("ATUALIZAR PIZZA".center(50))
print("-"*60)

try:
    codigo = int(input("\nDigite o código:"))
    sabor = input("Digite o sabor: ")
    preco = float(input("Preço R$: "))   
    comando = "UPDATE pizzas SET sabor = ?, preco = ? WHERE codigo = ?"
    cursor.execute(comando, (sabor,preco,codigo))
except ValueError:
    print("Erro: digite um valor R$ válido")
else:
    if cursor.rowcount > 0:
            # rowcount serve para informar quantas linhas forma alteradas
        print(f"\nPizza: '{sabor}' atualizada com sucesso!")
    else:
        print("Item não localizado com esse código")
            # valida se existe ou não o código

    conexao.commit()
finally:
    conexao.close()
print("-"*60)
# Explicação do uso de try, except e finally no código.
# try: executa um bloco de código que pode gerar exceções.
# except: trata os erros especificados, como ValueError ao converter
# uma entrada inválida para int ou float.
# finally: executa a etapa de finalização independentemente de ocorrer
# uma exceção ou não, sendo útil para liberar recursos, como fechar a conexão
# com o banco de dados. 