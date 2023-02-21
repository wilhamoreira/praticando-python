import os
os.system('cls')

temperatura_em_c = int(input('informe a temperatura em graus Celsius: '))

temperatura_em_f = ( ( 9 * (temperatura_em_c) / 5 ) ) + 32

print(f'\nA temperatura em Fahrenheit é {temperatura_em_f} F')
