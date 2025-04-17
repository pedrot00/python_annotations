import random

def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:    
        result  =  3 * number + 1
    print(result)
    return result

try:
    number = random.randint(1,1000)
    print(f'numero escolhido: {number}')
    while number!=1:
        number = collatz(number)

except ValueError as e:
    print(f'Error: {e}')
    print('Insira um valor inteiro amigo')
    