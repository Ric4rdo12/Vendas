#IMPORTAÇÕES
import os
from funcoes.operacoes.modificadores import adicionarVenda, removerVenda
from funcoes.tela.visualizacao import menu, verVenda
import json


try:
    with open('vendas.json', 'r', encoding='utf-8') as arquivo:
        total_vendas = json.load(arquivo)
except (FileNotFoundError, json.JSONDecodeError):
    total_vendas = []

#CÓDIGO PRINCIPAL
while True:
    menu()

    try:
        opcao = int(input('Sua escolha: '))
        os.system('cls' if os.name == 'nt' else 'clear')

    except (TypeError, ValueError):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\33[31mValor inválido! Tente novamente.\33[m') 
    else:
        if opcao == 1:
            adicionarVenda(total_vendas)
        elif opcao == 2:
            removerVenda(total_vendas)
        elif opcao == 3:
            verVenda(total_vendas)
        elif opcao == 4:
            exit()
        else:
            print('\33[31mValor inválido! Tente novamente.\33[m')
