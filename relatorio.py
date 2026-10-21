import sqlite3
from config import caminho_banco
import pandas as pd
from time import sleep


def relatorio():
    print("RELATÓRIO".center(50))
    conexao = sqlite3.connect(caminho_banco)
    try:
        sleep(2)
        df = pd.read_sql_query("SELECT * FROM pizzas",conexao)
        print(df.to_string(index=False))
        df.to_csv("pizzas_atualizado.csv",sep=";",index=False, encoding="utf-8-sig")
        print("\n\nGerando gelatório...")
        sleep(2)
        print("\nRelatório gerado e salvo com sucesso!")
    finally:
        conexao.close()
        # fecha SEMPRE


