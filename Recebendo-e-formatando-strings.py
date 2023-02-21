'''
Atribuas os valores a nome,idade e cidade-uf
imprima todos os dados mas a cidade (parnaiba) sem a UF
exemplo da impressão "parnaiba"
'''
import os
os.system('cls' if os.name == 'nt' else 'clear')

print('*'*20)
print('formatação de strings')
print('*'*20)

nome = input('Qual seu nome? \n')
idade = input('Qual a sua idade? \n')
cidade = input('informe a cidade e a uf CIDADE-UF \n')

print('*'*10)
print(f'Seu nome é  {nome} \nvocê tem  {idade} anos \ne mora em {cidade[0:len(cidade)-3]} ')
print('*'*10)
