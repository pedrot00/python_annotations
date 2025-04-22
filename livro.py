import sys
import os

# Função para limpar a tela
def limpar_tela():
    os.system('cls' if sys.platform.startswith('win') else 'clear')

# Dicionário de produtos com quantidades
produtos = {
    'detergente': 35,
    'desinfetante': 35,
    'vassoura': 35,
    'balde': 35
}

# Funções do CRUD
def inserir_produto():
    produto = input("Digite o nome do produto: ").lower()
    if produto in produtos:
        print("Produto já existe. Deseja adicionar mais unidades?")
        opcao = input("s/n: ").lower()
        if opcao == 's':
            quantidade = int(input("Digite a quantidade a adicionar: "))
            produtos[produto] += quantidade
    else:
        quantidade = int(input("Digite a quantidade: "))
        produtos[produto] = quantidade
    print(f"Produto '{produto}' adicionado/atualizado com sucesso!")

def buscar_produto():
    produto = input("Digite o nome do produto a buscar: ").lower()
    if produto in produtos:
        print(f"{produto}: {produtos[produto]} unidades")
    else:
        print("Produto não encontrado.")

def ler_produto():
    if not produtos:
        print("Estoque vazio.")
    else:
        print("Produtos em estoque:")
        for nome, qtd in produtos.items():
            print(f"{nome.ljust(15)} -> {qtd} unidades")

def atualizar_produto():
    produto = input("Digite o nome do produto a atualizar: ").lower()
    if produto in produtos:
        nova_qtd = int(input("Digite a nova quantidade: "))
        produtos[produto] = nova_qtd
        print("Produto atualizado com sucesso.")
    else:
        print("Produto não encontrado.")

def deletar_produto():
    produto = input("Digite o nome do produto a deletar: ").lower()
    if produto in produtos:
        del produtos[produto]
        print("Produto deletado com sucesso.")
    else:
        print("Produto não encontrado.")

def sair():
    print("Saindo do programa...")
    sys.exit()

# Função para mostrar o menu
def menu():
    print("\n--- MENU ESTOQUE ---")
    print("|1| Inserir produto")
    print("|2| Buscar produto")
    print("|3| Ler todos os produtos")
    print("|4| Atualizar produto")
    print("|5| Deletar produto")
    print("|6| Sair")

# Loop principal
while True:
    limpar_tela()
    totalItens = sum(produtos.values())
    print(f"Total de itens no estoque: {totalItens}")
    menu()

    try:
        escolha = int(input("\nDigite sua escolha: "))
    except ValueError:
        print("Digite um número válido.")
        input("Pressione Enter para continuar...")
        continue

    if escolha == 1:
        inserir_produto()
    elif escolha == 2:
        buscar_produto()
    elif escolha == 3:
        ler_produto()
    elif escolha == 4:
        atualizar_produto()
    elif escolha == 5:
        deletar_produto()
    elif escolha == 6:
        sair()
    else:
        print("Escolha inválida.")
    
    input("\nPressione Enter para continuar...")
