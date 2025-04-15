nome = input('Insira o seu nome: ')
base_calc = float(input('Insira a sua base de contribuição: '))

if base_calc <= 2259.20:
    ir = base_calc * 0
    print(f'{nome}, sua base de contribuição está na faixa entre R$ 0,00 e R$ 2259,20.')

elif base_calc <= 2826.65:
    ir = (base_calc * 0.075) - 169.44
    print(f'{nome}, sua base de contribuição está na faixa entre R$ 2259,21 e R$ 2826,65.')

elif base_calc <= 3751.05:
    ir = (base_calc * 0.15) - 381.44
    print(f'{nome}, sua base de contribuição está na faixa entre R$ 2826,66 e R$ 3751,05.')

elif base_calc <= 4664.68:
    ir = (base_calc * 0.225) - 662.77
    print(f'{nome}, sua base de contribuição está na faixa entre R$ 3751,06 e R$ 4664,68.')

else:
    ir = (base_calc * 0.275) - 896.00
    print(f'{nome}, sua base de contribuição está acima de R$ 4664,69.')

taxa_efetiva = (ir * 100) / base_calc
print(f'O valor do IR é: R$ {ir:.2f}')
print(f'Taxa efetiva: {taxa_efetiva:.1f}%')
