quantidade_notas = int(input('Digite a quantidade de notas: '))
soma_notas = 0

for i in range(1, quantidade_notas + 1):
    nota = float(input(f"Digite a nota {i}: "))
    soma_notas += nota
media = soma_notas / quantidade_notas
print(f"A média das notas é {media:.2f}.")