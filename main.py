# O que o main.py deverá fazer?
# 1. Centralizar a execução do sistema.
# 2. Exibir o menu principal da pizzaria.
# 3. Permitir que o usuário escolha uma operação.
# 4. Direcionar a execução para a funcionalidade correspondente.
# 5. Permitir que o usuário saia do sistema.

# ===============================================================
# Importando módulos


from atualizar import atualizar
from conferir import conferir
from excluir import excluir
from inserir import inserir


def menu():
    while True:
        print("=" * 60)
        print("🍕 PIZZARIA PYTHON 🍕".center(60))
        print("☰ MENU PRINCIPAL".center(60))
        print("=" * 60)

        print("\n1 - Atualizar pizza")
        print("2 - Conferir pizzas")
        print("3 - Excluir pizza")
        print("4 - Inserir pizza")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        print("=" * 60)

        if opcao == "1":
            atualizar()

        elif opcao == "2":
            conferir()

        elif opcao == "3":
            excluir()

        elif opcao == "4":
            inserir()

        elif opcao == "0":
            print("\nSaindo do sistema...")
            print("Até logo!")
            break

        else:
            print(f"\nOpção '{opcao}' inválida!")
            print("Opções válidas: 1, 2, 3, 4 ou 0.")


if __name__ == "__main__":
    try:
        menu()
    except Exception as erro:
        print(f"\n ❌ Erro inesperdo: {erro}")
    input("\n\nPressione ENTER para sair do programa.")
