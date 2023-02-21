'''
esceva uma programa que leia dois números e que pergunte qual a operação o usuario deseja
realizar. Você pode calcular soma(+), subtração(-), multiplicação(*) e divisão(/). exiba
o resultado da operação solicitada.
'''
import os
os.system('cls')
numero1 = int(input('Informe o primeiro numero : '))
operacao = input('Informe a operação ( + adição | - Subtração | * Multiplicação | / - Divisão ) : ')
numero2 = int(input('Informe o segundo numero: '))

if operacao == '+':
    print(f' {numero1} + {numero2} = {numero1+numero2}')
elif operacao == '-':
    print(f' {numero1} - {numero2} = {numero1-numero2}')
elif operacao == '/':
    if numero2 == 0:
        print('Impossivel dividir por zero!')
    else:
        print(f' {numero1} / {numero2} = {numero1/numero2}')
elif operacao == '*':
    print(f' {numero1} * {numero2} = {numero1*numero2}')
else:
    print('Informe uma operação valida!')