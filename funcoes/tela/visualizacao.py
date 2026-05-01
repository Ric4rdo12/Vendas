import os


def menu():
    print(f'{"PLATAFORMA DE VENDAS":-^40}')
    print("""1 -> Adicionar venda
2 -> Remover venda
3 -> Ver vendas
4 -> Editar venda
5 -> Buscar venda
6 -> Limpar vendas
7 -> Sair
""")


def verVenda(total_vendas):
    """Mostra relatório das vendas já registradas, mostrando todas as vendas e total de preço dividido
    em categorias (dinheiro, PIX, cartão e total) em baixo.

    Args:
        total_vendas (list): lista principal que armazena todas as vendas registradas.
    """
    if not total_vendas:
        print('\33[31mNenhuma venda registrada.\33[m')
        return
    
    total_dinheiro = sum(dinheiro["preco"] for dinheiro in total_vendas if dinheiro["forma_pagamento"] == 'Dinheiro')
    total_pix = sum(pix["preco"] for pix in total_vendas if pix["forma_pagamento"] == 'Pix')
    total_cartao = sum(cartao["preco"] for cartao in total_vendas if cartao["forma_pagamento"] in ('Crédito', 'Débito'))
    total_geral = sum(total["preco"] for total in total_vendas)

    nomes_vendidos = []
    contagem = {}
    for venda in total_vendas:
        nomes_vendidos.append(venda['nome'])
    
    for nome in nomes_vendidos:
        if nome in contagem:
            contagem[nome] += 1
        else:
            contagem[nome] = 1

    ranking = sorted(contagem, key=contagem.get, reverse=True)

    print(f'{"TABELA VENDAS":-^40}')
    for posicao, venda in enumerate(total_vendas):
        print(f'{posicao+1}° - {venda["nome"]} - R${venda["preco"]:.2f} - {venda["forma_pagamento"]}')
    print('--' * 20)
    print(f'Total em dinheiro: R${total_dinheiro:.2f}')
    print(f'Total em PIX: R${total_pix:.2f}')
    print(f'Total no cartão: R${total_cartao:.2f}')
    print(f'Total geral: R${total_geral:.2f}')
    print('--' * 20)
    print('PRODUTOS MAIS VENDIDOS')
    for produto in ranking[:3]:
        print(f'-> {produto}: {contagem[produto]} venda(s)')
    print('PRODUTOS MENOS VENDIDOS')
    for produto in reversed(ranking[-3:]):
        print(f'-> {produto}: {contagem[produto]} venda(s)')
    print('--' * 20)

    input('Pressione Enter para voltar ao menu.')
    os.system('cls' if os.name == 'nt' else 'clear')


def buscarVenda(total_vendas):
    """O usuário digita o nome da venda que ele quer buscar e será buscado todas as vendas com o nome
    digitado.

    Args:
        total_vendas (list): lista principal que armazena todas as vendas registradas.
    """
    if not total_vendas:
        print('\33[31mNenhuma venda registrada.\33[m')
        return
    
    nome_busca = input('Qual o nome da venda que deseja buscar? ').strip().title()
    print('--' * 20)
    encontrou = False
    for posicao, venda in enumerate(total_vendas):
        
        if nome_busca == venda['nome']:
            encontrou = True
            print(f'{posicao + 1}° - {venda['nome']} - R${venda['preco']:.2f} - {venda['forma_pagamento']}')
    
    if not encontrou:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'\33[31mNenhuma venda registrada como {nome_busca} foi encontrada.\33[m')
        return
    print('--' * 20)
    input('Pressione Enter para voltar ao menu.')
    os.system('cls' if os.name == 'nt' else 'clear')