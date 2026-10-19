import sqlite3

from config import caminho_banco


def excluir():
    print("=" * 60)
    print("EXCLUIR PIZZA".center(50))
    print("=" * 60)

    try:
        codigo = int(input("Informe o código: "))
    except ValueError:
        print("Código não localizado, informe um código válido.")
        return

    conexao = sqlite3.connect(caminho_banco)

    try:
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM pizzas WHERE Código = ?", (codigo,))
        retorno = cursor.fetchone()

        if retorno is None:
            print(f"\nCódigo: '{codigo}' não localizado.")
            return

        confirmacao = input("Deseja excluir? (s/n): ").strip().lower()

        if confirmacao == "s":
            cursor.execute("DELETE FROM pizzas WHERE Código = ?", (codigo,))
            if cursor.rowcount > 0:
                conexao.commit()
                print(f"\nPizza: {codigo}, excluída com sucesso!")
            else:
                print("Pizza não excluída.")
        else:
            print("Exclusão cancelada!")

        print("=" * 60)
    finally:
        conexao.close()