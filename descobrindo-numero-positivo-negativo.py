'''
Receba um número e verifique se ele é positivo ou negatio

'''
#limpando o terminal
import os
os.system('cls' if os.name == 'nt' else 'clear')

#recebendo um numero inteiro
numero = int(input('Informe um numero: '))

#fazendo as validações do numero para saber se é positivo ou negativo
if numero >= 0 :
    print(f'O numero {numero} é um numero POSITIVO ')
else:
    print(f'O numero {numero} é um numero NEGATIVO')
