ano_de_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = 2024

idade = ano_atual - ano_de_nascimento

if idade >= 16:
    print('Pode votar este ano!')
else:
    print('Não pode votar!')