import time
contador = 0
contador_ate_quanto = int(input('Informe até qual número contar: '))
elevado = int(input('Elevado a Quanto? '))

while contador < contador_ate_quanto:
    contador = contador + elevado
    print('Contador', int(contador))
    time.sleep(1)