import sqlite3
import pandas as pd
from config import caminho_banco

def conferir():
    # O que foi feito e alterado nesse código: 
    # Nesse código, foi implementado o uso da biblioteca Pandas junto com SQL
    # Para poder melhorar a apresentação do conteúdo dos bancos de dados.
    # Deixando o código mais legível e mais objetivo em sua execução.
    print("="*60)
    print("🍕 🍕 PIZZARIA PYTHON 🍕 🍕".center(50))
    print("="*60)
    print("📋 Nosso cardápio".center(50))
    print("-"*60)
    conexao = sqlite3.connect(caminho_banco)

    df = pd.read_sql_query(
        "\nSELECT * FROM pizzas",conexao
    )
    # index=False: esconde a coluna de numeração (0, 1, 2...) criada pelo pandas
    print(df.to_string(index=False))
    cursor = conexao.cursor()
    
    conexao.commit()
    conexao.close()

    
    
    





