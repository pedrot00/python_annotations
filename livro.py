lista1 = ['gato', 'cachorro', 'papagaio', 'elefante', 'girafa']
lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista3 = list('AAAAAAFAAAAAAA')

def mostrar_produto(codigo, info):
    print("Código:".ljust(12), codigo)
    print("Nome:".ljust(12), info['nome'])
    print("Valor:".ljust(12), f"{info['preço']:.2f} R$")
    print("Em estoque:".ljust(12), 'Sim' if info['estoque'] else 'Não')
    print("-" * 30)


produtos = {
    '0001': {'nome': 'Teclado gamer', 'preço': 150.00, 'estoque': True},
    '0002': {'nome': 'Mouse RGB', 'preço': 70.00, 'estoque': True},
    '0003': {'nome': 'Monitor 1444hz', 'preço': 1700.00, 'estoque': False},
    '0004': {'nome': 'Notebook Acer', 'preço': 2500.00, 'estoque': False},
}

#print(f'Eu quero um {produtos.get('0001', {}).get('nome', str(0))}')

print(produtos.setdefault('0005',{
    'nome': 'Mousepad', 'preço': 80.00, 'estoque': True
}))

#for codigo, info in produtos.items():

    # mostrar_produto(codigo, info)

