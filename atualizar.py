
import sqlite3


def atualizar():
    resposta = "S"

    while resposta != "N":
        conexao = sqlite3.connect("pizzaria.db")
        cursor = conexao.cursor()

        print("-" * 60)
        print("ATUALIZAR PIZZA".center(50))
        print("-" * 60)

        try:
            codigo = int(input("\nDigite o código: "))
            sabor = input("Digite o sabor: ")
            broto = float(input("Preço Broto R$: "))
            media = float(input("Preço Média R$: "))
            grande = float(input("Preço Grande R$: "))

            tipo = input(
                "Digite o tipo da pizza (Doce/Salgada): "
            ).strip().capitalize()

            if tipo not in ("Doce", "Salgada"):
                raise ValueError(
                    "O tipo deve ser Doce ou Salgada."
                )

            comando = """
                UPDATE pizzas
                SET "Sabor" = ?,
                    "Broto" = ?,
                    "Média" = ?,
                    "Grande" = ?,
                    "Tipo" = ?
                WHERE "Código" = ?
            """

            cursor.execute(
                comando,
                (sabor, broto, media, grande, tipo, codigo)
            )

        except ValueError as erro:
            print(f"\nErro: {erro}")

        else:
            if cursor.rowcount > 0:
                conexao.commit()
                print(f"\nPizza '{sabor}' atualizada com sucesso!")
            else:
                print(
                    f"\nCódigo {codigo} não localizado. "
                    "Nenhuma pizza foi atualizada."
                )

        finally:
            conexao.close()
            print("-" * 60)

        resposta = input(
            "\nDeseja atualizar outra pizza? [S/N]: "
        ).strip().upper()

    print("\nFinalizando atualização de pizzas!")


# Explicação do uso de try, except, else e finally.
# try: executa um bloco de código que pode gerar exceções.
# except: trata erros especificados, como ValueError ao converter
# uma entrada inválida para int ou float, ou ao validar o tipo.
# else: executa somente quando não ocorre exceção no bloco try.
# Neste código, verifica se alguma linha foi alterada e confirma
# a transação com commit().
# finally: executa independentemente de ocorrer uma exceção ou não.
# É útil para liberar recursos, como fechar a conexão com o banco.
#
# raise: gera uma exceção intencionalmente quando uma condição
# inválida é identificada, como um tipo diferente de Doce ou Salgada.
# .strip(): remove espaços em branco no início e no final do texto.
# .capitalize(): deixa a primeira letra maiúscula e as demais
# minúsculas, padronizando o tipo para Doce ou Salgada.
# while: repete a atualização enquanto resposta for diferente de "N".
