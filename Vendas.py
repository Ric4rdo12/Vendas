#plataforma de vendas, mostrar menu com as seguintes opções: adicionar venda, ver vendas (mostrando total delas), remover venda,
#ver lista de fiado e sair
#estrutura da venda: nome, preço, forma de pagamento

import os
import time

total_vendas = []
venda_atual = {}

while True:
    print(f'{"PLATAFORMA DE VENDAS":-^40}')
    print("""1 -> Adicionar venda
2 -> Remover venda
3 -> Ver vendas
4 -> Lista fiado
5 -> Sair
""")
    
    opcao = int(input('Sua escolha: '))
    os.system('cls')
    
    #ADICIONAR VENDA
    if opcao == 1:
        venda_atual['nome'] = str(input('Nome do produto: ')).strip().title()
        venda_atual['preco'] = float(input('Valor total da compra: R$'))
        
        
        while True:
            print("""1 -> Dinheiro
2 -> PIX
3 -> Crédito
4 -> Débito
5 -> Fiado""")
            pagar = int(input('Forma de pagamento: '))
            if pagar == 1:
                venda_atual['forma_pagamento'] = 'Dinheiro'
                break
            elif pagar == 2:
                venda_atual['forma_pagamento'] = 'PIX'
                break
            elif pagar == 3:
                venda_atual['forma_pagamento'] = 'Crédito'
                break
            elif pagar == 4:
                venda_atual['forma_pagamento'] = 'Débito'
                break
            elif pagar == 5:
                venda_atual['forma_pagamento'] = 'Fiado'
                break
            else:
                os.system('cls')
                print('\33[31mValor inválido. Tente novamente.\33[m')
        
        total_vendas.append(venda_atual.copy())
        
        
        os.system('cls')
        print('\33[32mVenda registrada com sucesso!\33[m')
        
     
    #REMOVER VENDAS
    elif opcao == 2:
        if not total_vendas:
            print('\33[31mNenhuma venda registrada.\33[m')
            continue
        else:
            while True:
                print(f'{"TABELA VENDAS":-^40}')
                for posicao, venda in enumerate(total_vendas):
                    print(f'{posicao+1}° - {venda["nome"]} - R${venda["preco"]:.2f} - {venda["forma_pagamento"]}')
                
                print('--' * 20)
                escolha = int(input('Qual venda você quer remover? (digite o número da venda) '))
                if 1 <= escolha <= len(total_vendas):
                    removed = total_vendas.pop(escolha - 1)
                    os.system('cls')
                    print(f'\33[32mA venda: {removed["nome"]} de R${removed["preco"]:.2f} paga com {removed["forma_pagamento"]} foi removida com sucesso!\33[m')
                    break
                else:
                    os.system('cls')
                    print(f'\33[33mNúmero inválido! Digite um número entre 1 e {len(total_vendas)} da posição da venda que você quer remover.\33[m')
    
    
    #VER VENDAS
    elif opcao == 3:
        if not total_vendas:
            print('\33[31mNenhuma venda registrada.\33[m')
            continue
        else:
            total_dinheiro = sum(dinheiro["preco"] for dinheiro in total_vendas if dinheiro["forma_pagamento"] == 'Dinheiro')
            total_PIX = sum(pix["preco"] for pix in total_vendas if pix["forma_pagamento"] == 'PIX')
            total_cartao = sum(cartao["preco"] for cartao in total_vendas if cartao["forma_pagamento"] == 'Crédito' or cartao["forma_pagamento"] == 'Débito')
            total_fiado = sum(fiado["preco"] for fiado in total_vendas if fiado["forma_pagamento"] == 'Fiado')
            total_geral = sum(total["preco"] for total in total_vendas)
            
            print(f'{"TABELA VENDAS":-^40}')
            for posicao, venda in enumerate(total_vendas):
                    print(f'{posicao+1}° - {venda["nome"]} - R${venda["preco"]:.2f} - {venda["forma_pagamento"]}')
            print('--' * 20)
            print(f'Total em dinheiro: R${total_dinheiro:.2f}')
            print(f'Total em PIX: R${total_PIX:.2f}')
            print(f'Total no cartão: R${total_cartao:.2f}')
            print(f'Total a prazo(fiado): R${total_fiado:.2f}')
            print(f'Total geral: R${total_geral:.2f}')
            print('--' * 20)
            
            
    #LISTA FIADO
    elif opcao == 4:
        fiados = [v for v in total_vendas if v['forma_pagamento'] == 'Fiado']
        
        if not fiados:
            print('\33[31mNenhuma venda paga com fiado registrada.\33[m')
            continue
        else:
            print(f'{"TABELA FIADO":-^40}')
            for posicao, venda in enumerate(fiados):
                print(f'{posicao+1}° - {venda["nome"]} - R${venda["preco"]:.2f}')
    
    
    #SAIR
    elif opcao == 5:
        print(f'{"Saindo...":-^40}')
        exit()
    
    #CASO DER ERRO
    else:
        print('\33[31mOpção inválida. Tente novamente.\33[m')