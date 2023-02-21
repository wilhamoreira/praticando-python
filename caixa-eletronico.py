import os
os.system('cls')

nota_cinquenta = 0
nota_vinte = 0
nota_dez = 0
nota_um = 0

valor_saque = 1
while valor_saque != 0:
    try:
        valor_saque = int(input('Informe qual valor que você deseja sacar (digite 0 para sair) :  '))
        if valor_saque == 0:
            break
        else:
            nota_cinquenta = int(valor_saque / 50)
            resto = valor_saque % 50

            nota_vinte = int(resto / 20)
            resto = resto % 20

            nota_dez = int(resto / 10)
            resto = resto % 10

            nota_um = resto
            break
    except:
        print('Valor invalido! Digite nota_um nnota_umero inteiro')
        continue

if nota_cinquenta > 0:
    if nota_cinquenta == 1:
      print(f'{nota_cinquenta} nota de R$ 50')
    else:
      print(f'{nota_cinquenta} notas de R$ 50')

if nota_vinte > 0:
    if nota_vinte == 1:
      print(f'{nota_vinte} nota de R$ 20')
    else:
      print(f'{nota_vinte} notas de R$ 20')

if nota_dez > 0:
    if nota_dez == 1:
      print(f'{nota_dez} nota de R$ 10')
    else:
      print(f'{nota_dez} notas de R$ 10')

if nota_um > 0:
    if nota_um == 1:
      print(f'{nota_um} nota de R$ 1')
    else:
      print(f'{nota_um} notas de R$ 1')
