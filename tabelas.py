destino = [
    'Florianópolis',
    'Porto Alegre',
    'São Paulo', 
    'Belo Horizonte', 
    'Salvador'
]

distancia = [307, 741, 416, 992, 1349]

clientes = [
    ['Duda Magazine', 30, 20, 28, 23, 24], 
    ['Ponto Quente', 35, 120, 38, 53, 23],
    ['Paraibana', 45, 80, 58, 63, 13],
    ['Paulistão', 65, 40, 68, 33, 11],
    ['Cascavel Mart', 75, 50, 18, 53, 25],
    ['Zanata Tec', 25, 30, 108, 33, 57]
]

frete = 6.90
print(f'O momento do frete é de R$ {frete:.2f}')

reajuste = float(input('Reajuste desejado para o momento do frete (+/- %): '))
frete += (frete * reajuste / 100)

# Cálculo das toneladas por cidade
toneladas_por_cidade = [0] * len(destino)
for cliente in clientes:
    for i in range(len(destino)):
        toneladas_por_cidade[i] += cliente[i + 1]

# Cálculo do faturamento por cidade
faturamento_por_cidade = []
for i in range(len(destino)):
    faturamento = toneladas_por_cidade[i] * distancia[i] * frete
    faturamento_por_cidade.append(faturamento)

# Faturamento total
faturamento_total = sum(faturamento_por_cidade)

# Cidades com maior/menor faturamento
maior_faturamento = max(faturamento_por_cidade)
menor_faturamento = min(faturamento_por_cidade)
cidade_maior = destino[faturamento_por_cidade.index(maior_faturamento)]
cidade_menor = destino[faturamento_por_cidade.index(menor_faturamento)]

# Impressão do relatório
print("\nRelatório 1 - Faturamento - Transportadora InovaLOG")
print("-" * 90)
header = f"{'Cliente':<18}" + "".join([f"{city:<15}" for city in destino])
print(header)
print("-" * 90)

for cliente in clientes:
    linha = f"{cliente[0]:<18}"
    for valor in cliente[1:]:
        linha += f"{valor:<15.2f}"
    print(linha)

print("-" * 90)
linha_totais = f"{'Total (t)':<18}" + "".join([f"{t:<15.2f}" for t in toneladas_por_cidade])
print(linha_totais)

print("-" * 90)
linha_faturamento = f"{'Total (R$)':<18}" + "".join([f"{f:<15.2f}" for f in faturamento_por_cidade])
print(linha_faturamento)

print("-" * 90)
print(f"Faturamento total: R$ {faturamento_total:.2f}")
print(f"Destino de maior faturamento: {cidade_maior} (R$ {maior_faturamento:.2f})")
print(f"Destino de menor faturamento: {cidade_menor} (R$ {menor_faturamento:.2f})")


faturamento_por_cliente = [0] * len(clientes)
for idx, cliente in enumerate(clientes):
    faturamento = 0
    for valor in cliente:
        if isinstance(valor, int):
            faturamento += valor
    faturamento_por_cliente[idx] = faturamento


valorPago = []  # lista com tuplas (nome, valor total)
for cliente in clientes:

    toneladas = cliente[1:]
    total = 0
    for d, t in zip(distancia, toneladas):
        total += d * t * frete
    valorPago.append(total)

idx_maior = valorPago.index(max(valorPago))
idx_menor = valorPago.index(min(valorPago))



print("\nRelatório 2 - Clientes - Transportadora InovaLOG")
print("-" * 130)
header = f"{'Cliente':<18}" + "".join([f"{city:<18}" for city in destino]) + f"{'Total (t)':<12}{'Total (R$)':<12}"
print(header)
print("-" * 130)

for i, cliente in enumerate(clientes):
    nome = cliente[0]
    toneladas = cliente[1:]
    total_toneladas = sum(toneladas)
    total_valor = valorPago[i]
    linha = f"{nome:<18}"
    for t in toneladas:
        linha += f"{t:<18.2f}"
    linha += f"{total_toneladas:<12.2f}{total_valor:<12.2f}"
    print(linha)

print("-" * 130)
print(f"Cliente responsável pelo menor valor pago: {clientes[idx_menor][0]}")
print(f"Cliente responsável pelo maior valor pago: {clientes[idx_maior][0]}")
