import sqlite3
from pathlib import Path
from config import caminho_banco
import pandas as pd
from time import sleep

PASTA_PROJETO = Path(__file__).parent

def relatorio():
    print("RELATÓRIO".center(50))
    conexao = sqlite3.connect(caminho_banco)
    try:
        sleep(2)
        df = pd.read_sql_query("SELECT * FROM pizzas",conexao)
        print(df.to_string(index=False))

        caminho_csv = PASTA_PROJETO / "pizzas_atualizado.csv"
       
        df.to_csv(caminho_csv,sep=";",index=False, encoding="utf-8-sig")
        print("\n\nGerando relatório...")
        sleep(2)
        print("\nRelatório gerado e salvo com sucesso!")
    finally:
        conexao.close()
        # fecha SEMPRE


