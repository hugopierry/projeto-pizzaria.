# O que o main.py deverá fazer?

# A ideia é centralizar a execução do sistema:
# 1. Exibir o menu principal da pizzaria.
# 2. Permitir que o usuário escolha uma operação.
# 3. Direcionar a execução para a funcionalidade correspondente.
# 4. Permitir que o usuário saia do sistema.

#===============================================================
# importando módulos:

from atualizar import atualizar
from conferir import conferir
from excluir import excluir
from inserir import inserir

def menu():
    while True:
        print("-"*60)
        print("PIZZARIA".center(50))
        print("1 - Atualizar pizza")
        print("2 - Conferir pizza")
        print("3 - Excluir pizza")
        print("4 - Inerir pizza")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            atualizar()
        elif opcao == "2":
            conferir()
        elif opcao =="3":
            excluir()
        elif opcao == "4":
            inserir()
        elif opcao == "0":
            print("Saindo...")
            print("Até logo")
            break
        else:
            print(f"Opção:'{opcao}', inválida! Informe uma opção válida.")
            print("Opçãoes: 1,2,3,4,0.")
        print("-"*60)
if __name__ == "__main__":
    menu()


