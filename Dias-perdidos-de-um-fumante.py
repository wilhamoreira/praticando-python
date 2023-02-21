import os
os.system('cls')

qte_cigarro_por_dia = int(input('Informe a quantidade de cigarros fumados por dia: '))
qte_anos_fumante = int(input('A quantos anos você ja é fumante: '))

qte_minutos = qte_cigarro_por_dia * 10
qte_anual = qte_minutos * 365
qte_dias_perdidos = (qte_anual/1440)*qte_anos_fumante


print(f' {qte_dias_perdidos:.2f} dias perdidos')
