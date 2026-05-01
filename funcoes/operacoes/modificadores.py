import os
import json


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
                    with open('vendas.json', 'w', encoding='utf-8') as arquivo:
                        json.dump(total_vendas, arquivo, indent=4, ensure_ascii=False)
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
                with open('vendas.json', 'w', encoding='utf-8') as arquivo:
                    json.dump(total_vendas, arquivo, indent=4, ensure_ascii=False)
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'\33[32mA venda: {removed["nome"]} de R${removed["preco"]:.2f} paga com {removed["forma_pagamento"]} foi removida com sucesso!\33[m')
                return
        
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'\33[33mNúmero inválido! Digite um número entre 1 e {len(total_vendas)} da posição da venda que você quer remover.\33[m')


def editarVenda(total_vendas):
    """Edita nome, preço ou forma de pagamento de uma venda de acordo com a posição dela

    Args:
        total_vendas (list): lista principal que armazena todas as vendas registradas.
    """
    if not total_vendas:
        print('\33[31mNenhuma venda registrada.\33[m')
        return
    
    while True:
        print(f'{"EDITAR VENDA":-^40}')
        for posicao, venda in enumerate(total_vendas):
            print(f'{posicao+1}° - {venda["nome"]} - R${venda["preco"]:.2f} - {venda["forma_pagamento"]}')
        print('--' * 20)
        try:
            escolha = int(input('Qual venda você quer editar? (digite a posição da venda) ')) - 1
            if 0 <= escolha <= len(total_vendas) - 1:
                print('1 -> Nome\n2 -> Preço\n3 -> Forma de pagamento')
                editar = int(input('O que quer editar? Digite o número do campo: '))
                print('--' * 20)
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'\33[33mNúmero inválido! Digite um número entre 1 e {len(total_vendas)} da posição da venda que você quer remover.\33[m')
                continue

        except (ValueError, TypeError):
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\33[31mValor inválido! Tente novamente.\33[m')
            continue

        else:
            if editar == 1:
                print(f'Nome atual: {total_vendas[escolha]['nome']}')
                total_vendas[escolha]['nome'] = input('Novo nome: ').strip().title()
                
                with open('vendas.json', 'w', encoding='utf-8') as arquivo:
                    json.dump(total_vendas, arquivo, indent=4, ensure_ascii=False)

                os.system('cls' if os.name == 'nt' else 'clear')
                print('\33[32mNome alterado com sucesso!\33[32m')
                break

            elif editar == 2:
                while True:
                    try:
                        print(f'Preço atual: {total_vendas[escolha]['preco']}')
                        total_vendas[escolha]['preco'] = float(input('Novo preço: '))
                
                    except (ValueError, TypeError):
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('\33[31mValor inválido! Tente novamente.\33[m')
                        continue

                    with open('vendas.json', 'w', encoding='utf-8') as arquivo:
                        json.dump(total_vendas, arquivo, indent=4, ensure_ascii=False)

                    os.system('cls' if os.name == 'nt' else 'clear')
                    print('\33[32mPreço alterado com sucesso!\33[m')
                    break
                break

            elif editar == 3:
                formas_de_pagamento = {
                    '1': 'Dinheiro',
                    '2': 'Pix',
                    '3': 'Crédito',
                    '4': 'Débito'
                    }
                
                while True:
                    print(f'Forma de pagamento atual: {total_vendas[escolha]["forma_pagamento"]}')
                    for chave, valor in formas_de_pagamento.items():
                        print(f'{chave} -> {valor}')
                    escolha_pagamento = input('Qual a nova forma de pagamento? ')

                    if escolha_pagamento in formas_de_pagamento:
                        total_vendas[escolha]['forma_pagamento'] = formas_de_pagamento[escolha_pagamento]

                        with open('vendas.json', 'w', encoding='utf-8') as arquivo:
                            json.dump(total_vendas, arquivo, indent=4, ensure_ascii=False)
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('\33[32mForma de pagamento alterada com sucesso!\33[m')
                        break

                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('\33[31mValor inválido! Tente novamente.\33[m')
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('\33[31mValor inválido! Tente novamente.\33[m')


def limparVendas(total_vendas):
    """Limpa todas as vendas já registradadas na lista e no JSON

    Args:
        total_vendas (list): lista principal que armazena todas as vendas registradas.
    """
    if not total_vendas:
        print('\33[31mNenhuma venda registrada.\33[m')
        return
    
    escolha = ' '
    while escolha not in 'SN':
        try:
            escolha = input('Você tem certeza que quer limpar todas as vendas? (S/N) ').strip().upper()[0]
        except (IndexError):
            os.system('cls' if os.name == 'nt' else 'clear')
            print('\33[31mValor inválido! Tente novamente.\33[m')
            continue
        else:
            if escolha == 'S':
                print('Limpando todas as vendas.')
                total_vendas.clear()
                with open('vendas.json', 'w', encoding='utf-8') as arquivo:
                    json.dump(total_vendas, arquivo, indent=4, ensure_ascii=False)
                os.system('cls' if os.name == 'nt' else 'clear')
                print('\33[32mVendas limpadas com sucesso!\33[m')
                return
            
            elif escolha == 'N':
                os.system('cls' if os.name == 'nt' else 'clear')
                print('\33[32mCancelamento da função limpar vendas.\33[m')
                return
            
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('\33[31mValor inválido!. Tente novamente.\33[m')