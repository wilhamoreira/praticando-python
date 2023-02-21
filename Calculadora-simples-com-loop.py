'''
esceva uma programa que leia dois números e que pergunte qual a operação o usuario deseja
realizar. Você pode calcular soma(+), subtração(-), multiplicação(*) e divisão(/). exiba
o resultado da operação solicitada.
'''
import os
os.system('cls')
decisao = 's'

while decisao in ('SIM', 's', 'S'):
    numero1 = int(input('Informe o primeiro numero : '))
    operacao = input('Informe a operação ( + adição | - Subtração | * Multiplicação | / - Divisão ) : ')
    numero2 = int(input('Informe o segundo numero: '))

    if operacao == '+':
        print(f' {numero1} + {numero2} = {numero1+numero2}')
        decisao = input('Voce deseja continuar ? S - Sim ou n - Não: ')
        os.system('cls')
    elif operacao == '-':
        print(f' {numero1} - {numero2} = {numero1-numero2}')
        decisao = input('Voce deseja continuar ? S - Sim ou n - Não: ')
    elif operacao == '/':
        if numero2 == 0:
            print('Impossivel dividir por zero!')
            decisao = input('Voce deseja continuar ? S - Sim ou n - Não: ')
            os.system('cls')
        else:
            print(f' {numero1} / {numero2} = {numero1/numero2}')
            decisao = input('Voce deseja continuar ? S - Sim ou n - Não: ')
            os.system('cls')
    elif operacao == '*':
        print(f' {numero1} * {numero2} = {numero1*numero2}')
        decisao = input('Voce deseja continuar ? S - Sim ou n - Não: ')
        os.system('cls')
    else:
        print('Informe uma operação valida!')
        decisao = input('Voce deseja continuar ? S - Sim ou n - Não: ')
        os.system('cls')
else:
    print('Fim do programa ')
