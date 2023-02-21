import os
os.system('cls')
lista = ['s']

while True:


    opcao = input('voce deseja adicionar ou remover elemento? A - adicionar | R - remover: ')

    if opcao == 'a':
        os.system('cls')
        adicionar = input('informe o elemento para adicioanr: ')
        lista.append(adicionar)
    elif opcao == 'r':
        os.system('cls')
        remover = input('informe o elemento para adicioanr: ')
        lista.remove(remover)
    else:
        break
    print(f'Lista atual {lista}')

print(lista)



