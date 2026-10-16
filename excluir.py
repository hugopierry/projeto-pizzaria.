import sqlite3

import conferir
import sys

conexao = sqlite3.connect("pizzaria.db")
cursor = conexao.cursor()

print("EXCLUIR PIZZA".center(50))

# 1. Pede o código
codigo = int(input("Informe o código: "))
# 2. Consulta o banco
cursor.execute("SELECT * FROM pizzas WHERE codigo = ?", (codigo,))
retorno = cursor.fetchone()
print(retorno)
# 3. Se não achou: avisa e encerra
if retorno is None:
   print(f"\nCódigo: '{codigo}' não localizado.")
   sys.exit()
# 4. Se achou: pergunta a confirmação
confirmacao = input("Deseja excluir? (s/n): ").strip().lower()
# 5. Se "S": executa o DELETE e avisa
if confirmacao == "s":
    comando_excluir = "DELETE FROM pizzas WHERE codigo = ?"
    cursor.execute(comando_excluir, (codigo,))
    if cursor.rowcount > 0:
        print(f"\nPizza: {codigo}, excluida com sucesso!")
    else:
        print("Pizza não excluída.")
else:
    # 6. Se não for "S": avisa que cancelou
    print("Exclusão cancelada!")

    
            
conexao.commit()
conexao.close()