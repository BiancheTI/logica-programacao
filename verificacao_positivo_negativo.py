numero = 0
numero = int(input('Informe o número: '))
if numero > 0:
    print(int(numero), 'É Positivo!')
elif numero == 0:
    print(int(numero), 'Nem positivo, nem negativo.')
else:
    print(int(numero), 'É Negativo!')