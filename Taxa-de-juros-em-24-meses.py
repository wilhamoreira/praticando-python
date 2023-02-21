'''
escreva um programa onde o usuario informe o valor do deposito inicial
e depois informe o valor da taxa de juros. imprima usando o while
o valor do saldo mensalmente durante 24 meses.
'''
import os
os.system('cls')

contador = 1


deposito = int(input('Informe o valor do deposito: '))
valor_mensal = deposito
taxa_juros = float(input('Informe o valor da taxa de juros: '))

taxa = taxa_juros / 100

while contador <= 24:
    valor_mensal += valor_mensal * taxa
    print(f' Saldo no {contador}º  mês - {valor_mensal:.2f} ')        
    contador = contador + 1