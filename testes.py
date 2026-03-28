total = [{'nome': 'Friskies'}]
for posicao, valor in enumerate(total):
    print(f'{valor['nome']} -> {posicao}°')
    
cu = int(input('sua escolha: '))

if cu > 0 or cu >= len(total):
    print('n ta dentro')
else:
    print('ta dentro')
    
for p in total:
    if p["nome"] == 'Friskies':
        print(p['nome'])