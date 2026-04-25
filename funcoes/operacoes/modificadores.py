import os


def adicionarVenda(total_vendas):
    """Adiciona a venda registrada na lista total_vendas, sendo a estrutura (em ordem): nome, preço e
    forma de pagamento.

    Args:
        total_vendas (list): lista principal que armazena todas as vendas registradas.
    """
    formas_de_pagamento = {
        '1': 'Dinheiro',
        '2': 'Pix',
        '3': 'Crédito',
        '4': 'Débito'
    }
    
    venda_atual = {}
    while True:
        try:
            venda_atual['nome'] = input('Nome do produto: ').strip().title()
            venda_atual['preco'] = float(input('Valor do produto: R$'))

        except (ValueError, TypeError):
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\33[31mValor(es) inválido(s). Tente novamente.\33[m')
            continue

        else:
            while True:
                for chave, valor in formas_de_pagamento.items():
                    print(f'{chave} -> {valor}')
                escolha_pagamento = input('Qual a forma de pagamento? ')

                if escolha_pagamento in formas_de_pagamento:
                    venda_atual['forma_pagamento'] = formas_de_pagamento[escolha_pagamento]
                    total_vendas.append(venda_atual.copy())
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('\33[32mVenda registrada com sucesso!\33[m')    
                    break
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('\33[33mValor inválido. Tente novamente.\33[m')
        break


def removerVenda(total_vendas):
    """Remove uma venda registrada da lista total_vendas, mas pode remover apenas uma venda por vez.

    Args:
        total_vendas (list): lista principal que armazena todas as vendas registradas.
    """
    if not total_vendas:
        print('\33[31mNenhuma venda registrada.\33[m')
        return
    
    while True:
        try:
            print(f'{"REMOVER VENDA":-^40}')
            for posicao, venda in enumerate(total_vendas):
                print(f'{posicao+1}° - {venda["nome"]} - R${venda["preco"]:.2f} - {venda["forma_pagamento"]}')
            print('--' * 20)
            escolha = int(input('Qual venda você quer remover? (digite a posição da venda) '))

        except (ValueError, TypeError):
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\33[31mValor inválido! Tente novamente.\33[m')
            continue
        
        else:
            if 1 <= escolha <= len(total_vendas):
                removed = total_vendas.pop(escolha - 1)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'\33[32mA venda: {removed["nome"]} de R${removed["preco"]:.2f} paga com {removed["forma_pagamento"]} foi removida com sucesso!\33[m')
                return
        
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'\33[33mNúmero inválido! Digite um número entre 1 e {len(total_vendas)} da posição da venda que você quer remover.\33[m')