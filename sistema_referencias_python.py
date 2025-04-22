import os
import sys

def limpar_tela():
    os.system('cls' if sys.platform.startswith('win') else 'clear')

