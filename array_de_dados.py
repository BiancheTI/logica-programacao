alunos = []
qtd = int(input('Digite a quantidade de alunos: '))
for i in range(qtd):
    nome = input('Digite o nome: ')
    idade = input('Digite a idade: ')
    nota = input('Digite a nota: ')
    aluno = {'nome': nome, 'idade': idade, 'nota': nota}
    alunos.append(aluno)
    print('*************************')
for aluno in alunos:
    print(f'nome: {aluno['nome']}, idade: {aluno['idade']}, nota: {aluno['nota']}')