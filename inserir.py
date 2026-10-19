
import sqlite3


def inserir():
    conexao = sqlite3.connect("pizzaria.db")
    cursor = conexao.cursor()


   
    # Laço de repetição (While) criado para controlar o fluxo do sistema.

    resposta = "S"
    while resposta !="N":
        try:
            
            print("INSERIR PIZZA: " .center(50))
            print("="*60)
            codigo = int(input("\nDigite o código: "))
            sabor = input("Digite o sabor: ")
            broto = float(input("Broto R$: "))
            media = float(input("Média R$: "))
            grande = float(input("Grande R$: "))
            comando_inserir = 'INSERT INTO pizzas ("Código", "Sabor", "Broto", "Média", "Grande") VALUES (?, ?, ?, ?, ?)'
            cursor.execute(comando_inserir, (codigo,sabor,broto,media,grande))
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



