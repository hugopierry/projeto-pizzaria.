## Sobre o projeto

Este projeto foi desenvolvido para praticar a metodologia **CRUD (Create, Read, Update e Delete)** utilizando Python e SQLite.

O programa simula um pequeno cadastro de pizzaria, permitindo armazenar e gerenciar código, sabor, tipo (doce ou salgada) e um preço para cada tamanho (Broto, Média e Grande).

## Funcionalidades

- **`criar.py`** — cria o banco de dados e a tabela `pizzas`. Uso exclusivo do desenvolvedor, rodado uma vez.
- **`inserir.py`** — cadastra novas pizzas com código, sabor, tipo e os preços Broto, Média e Grande.
- **`conferir.py`** — consulta e apresenta de forma organizada os dados cadastrados no banco de dados.
- **`atualizar.py`** — atualiza sabor, tipo e os preços Broto, Média e Grande de uma pizza, localizada pelo código.
- **`excluir.py`** — exclui uma pizza do banco de dados a partir do código informado.
- **`main.py`** — ponto de entrada do sistema, com o menu interativo para executar as operações.
- **`config.py`** — define o caminho do banco de dados, usado por todos os arquivos.

## Como executar

**1. Instale o pandas:**
```
pip install pandas
```

**2. Crie o banco (só na primeira vez):**
```
python criar.py
```

**3. Inicie o programa:**
```
python main.py
```

## Tecnologias utilizadas

- Python
- SQLite3
- SQL
- Pandas
- Power BI

## Roadmap

1. [x] Implementar tratamento de erros com `try`, `except` e `finally`.
2. [x] Criar um menu interativo no arquivo `main.py`, reunindo as operações CRUD em um único programa.
3. [x] Desenvolver um dashboard no Power BI para apresentar indicadores e gráficos a partir dos dados do banco de dados.

## Dashboard

![Dashboard Pizzaria Python](imagens/dashboard.png)

## Objetivo

Este projeto faz parte dos meus estudos práticos de programação e análise de dados. O objetivo é consolidar os fundamentos de Python e SQL e evoluir gradualmente para projetos de análise e visualização de dados, conectando essas habilidades ao Power BI.