
import sqlite3

conexao = sqlite3.connect("pizzaria.db")
cursor = conexao.cursor()

resposta = "S"
print("-"*60)
# Laço de repetição (While) criado para controlar o fluxo do sistema.

while resposta !="N":
    try:
        print("-"*60)
        print("INSERIR PIZZA: " .center(50))
        print("-"*60)
        codigo = int(input("\nDigite o código: "))
        sabor = input("Digite o sabor: ")
        preco = float(input("Preço R$: "))
        comando_inserir = "INSERT INTO pizzas (codigo, sabor, preco) VALUES (?,?,?)"
        cursor.execute(comando_inserir, (codigo,sabor,preco))
        conexao.commit()
        
    except ValueError:
        print("Código ou preço inválido. Informe valores numéricos.")
        continue
        # continue serve para interromper a execução da repetição atual e voltar ao
        # início do laço, sem executar as instruções que vêm depois dele naquela volta
    except sqlite3.IntegrityError:
    # except sqlite3.IntegrityError: Código que capitura e informa duplicidade de dados
        print("Esse código já está cadastrado, favor, informar um novo código.")
        continue
    print(f"\nPizza: '{sabor}' inserida com sucesso!")
    resposta = input("\nContinuar? : [S/N] ").strip().upper()
    
    
    
    
print("\nFeito!")
conexao.close()



