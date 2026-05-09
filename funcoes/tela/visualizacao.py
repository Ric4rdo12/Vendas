import os
from rich import print
from rich.panel import Panel
from rich.table import Table


def menu():
    print(Panel("""1 -> Adicionar venda
2 -> Remover venda
3 -> Ver vendas
4 -> Editar venda
5 -> Buscar venda
6 -> Limpar vendas
7 -> Sair
""", title='Menu Vendas', style='blue', width=25))


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

    mostrarVendas(total_vendas)

    print(Panel(f'Dinheiro: R${total_dinheiro:.2f}\n'
    f'PIX: R${total_pix:.2f}\n'
    f'Cartão: R${total_cartao:.2f}\n'
    f'Geral: R${total_geral:.2f}',
    title='💰 Totais', expand=False))

    print(Panel(
    '\n'.join(f'🏆 {produto}: {contagem[produto]} venda(s)' for produto in ranking[:3]),
    title='🥇 Produtos Mais Vendidos',
    style='cyan', expand=False))

    input('Pressione Enter para voltar ao menu.')
    os.system('cls' if os.name == 'nt' else 'clear')


def buscarVenda(total_vendas):
    """O usuário digita o nome da venda que ele quer buscar e será buscado todas as vendas com o nome
    digitado.

    Args:
        total_vendas (list): lista principal que armazena todas as vendas registradas.
    """
    if not total_vendas:
        msgErro('Nenhuma venda registrada.')
        return
    
    nome_busca = input('Qual o nome da venda que deseja buscar? ').strip().title()
    encontrou = False

    tabela = Table(title=f'Busca: {nome_busca}', show_lines=True)
    tabela.add_column('Posição')
    tabela.add_column('Produto')
    tabela.add_column('Preço')
    tabela.add_column('Pagamento')

    for posicao, venda in enumerate(total_vendas):
        if nome_busca == venda['nome']:
            encontrou = True
            tabela.add_row(f'{posicao + 1}°', venda['nome'], f"R${venda['preco']:.2f}", venda['forma_pagamento'])
    
    if not encontrou:
        os.system('cls' if os.name == 'nt' else 'clear')
        msgErro(f'Nenhuma venda registrada como {nome_busca} foi encontrada.')
        return

    print(tabela)
    input('Pressione Enter para voltar ao menu.')
    os.system('cls' if os.name == 'nt' else 'clear')


def msgSucesso(mensagem='Venda registrada com sucesso!'):
    print(Panel(mensagem, title='✅ Sucesso', style='green', expand=False))


def msgErro(mensagem='Valor inválido! Tente novamente.'):
    print(Panel(mensagem, title='❌ Erro', style='red', expand=False))


def mostrarVendas(total_vendas):
    tabela = Table(title='Tabela vendas', show_lines=True)

    tabela.add_column('Posição')
    tabela.add_column('Produto')
    tabela.add_column('Preço')
    tabela.add_column('Pagamento')

    for posicao, venda in enumerate(total_vendas):
        tabela.add_row(f'{posicao+1}°', venda['nome'], f"R${venda['preco']:.2f}", venda['forma_pagamento'])
    print(tabela)