import sqlite3
import pandas as pd

def conferir():
    # O que foi feito e alterado nesse código: 
    # Nesse código, foi implementado o uso da biblioteca Pandas junto com SQL
    # Para poder melhorar a apresentação do conteúdo dos bancos de dados.
    # Deixando o código mais legível e mais objetivo em sua execução.
    print("-"*60)
    print("CONFERIR".center(50))
    print("-"*60)
    conexao = sqlite3.connect("pizzaria.db")

    df = pd.read_sql_query(
        "SELECT * FROM pizzas",conexao
    )
    # index=False: esconde a coluna de numeração (0, 1, 2...) criada pelo pandas
    print(df.to_string(index=False))
    print("-"*60)
    conexao.close()
    





