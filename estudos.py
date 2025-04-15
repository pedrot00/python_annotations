import pandas as pd
from tabulate import tabulate

# Lista de produtos
produtos = [
    {'Produto': 'Arroz', 'Preço': 18.90, 'Distribuidora': 'Cerealista Sul'},
    {'Produto': 'Feijão', 'Preço': 9.20, 'Distribuidora': 'Cerealista Sul'},
    {'Produto': 'Macarrão', 'Preço': 5.60, 'Distribuidora': 'Massas Itália'},
    {'Produto': 'Óleo de soja', 'Preço': 7.80, 'Distribuidora': 'CooperÓleo'},
    {'Produto': 'Detergente', 'Preço': 2.50, 'Distribuidora': 'LimpaBem'},
    {'Produto': 'Sabão em pó', 'Preço': 12.00, 'Distribuidora': 'LimpaBem'},
    {'Produto': 'Açúcar', 'Preço': 4.70, 'Distribuidora': 'DoceVida'},
    {'Produto': 'Café', 'Preço': 16.00, 'Distribuidora': 'Grãos Brasil'},
    {'Produto': 'Leite', 'Preço': 4.30, 'Distribuidora': 'Laticínios Vale'},
    {'Produto': 'Farinha de trigo', 'Preço': 3.90, 'Distribuidora': 'Pães&Cia'},
    {'Produto': 'Achocolatado', 'Preço': 6.80, 'Distribuidora': 'ChocoMix'},
    {'Produto': 'Biscoito recheado', 'Preço': 3.20, 'Distribuidora': 'Biscoitão'},
    {'Produto': 'Margarina', 'Preço': 4.50, 'Distribuidora': 'Laticínios Vale'},
    {'Produto': 'Refrigerante', 'Preço': 6.00, 'Distribuidora': 'RefriTop'},
    {'Produto': 'Suco de uva', 'Preço': 9.90, 'Distribuidora': 'SucoBom'},
    {'Produto': 'Papel higiênico', 'Preço': 10.50, 'Distribuidora': 'PapelMais'},
    {'Produto': 'Sabonete', 'Preço': 1.80, 'Distribuidora': 'HigiClean'},
    {'Produto': 'Escova de dente', 'Preço': 3.70, 'Distribuidora': 'HigiClean'},
    {'Produto': 'Shampoo', 'Preço': 11.90, 'Distribuidora': 'HigiClean'},
    {'Produto': 'Desodorante', 'Preço': 8.50, 'Distribuidora': 'HigiClean'}
]


# Criar DataFrame e ordenar por nome do produto
df = pd.DataFrame(produtos)
df_ordenado = df.sort_values(by='Produto')

# Exibir como tabela formatada
print(tabulate(df_ordenado, headers='keys', tablefmt='fancy_grid', showindex=False))
