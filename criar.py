import sqlite3

from config import caminho_banco

# Script de setup: rodar só uma vez, manualmente (não passa pelo main.py).
# Descomente apenas a migração que precisa e rode.

conexao = sqlite3.connect(caminho_banco)

try:
    cursor = conexao.cursor()

    # cursor.execute('ALTER TABLE pizzas ADD COLUMN "Tipo" TEXT')
    # conexao.commit()
    # print("Coluna adicionada com sucesso!")

finally:
    conexao.close()

input("\nPressione ENTER para sair.")