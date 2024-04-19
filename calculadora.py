valor1 = float(input('Informe o primeiro valor: '))
operacao = str(input('Informe a operação: '))
valor2 = float(input('Informe o segundo valor: '))
resultado = 0
if operacao == '+':
    resultado = valor1 + valor2
elif operacao == '-':
    resultado = valor1 - valor2
elif operacao == '*':
    resultado = valor1 * valor2
elif operacao == '/':
    resultado = valor1 / valor2
else:
    print('Operação Invalida!')
print('Resultado: ',float(resultado))