from time import sleep
from funcoes.interface.interface import *
from funcoes.arquivo.arquivo import *
alunos = list()

while True:
    sleep(1.3)
    cabecalho()
    print('[1] Cadastrar novo aluno')
    print('[2] Listar alunos')
    print('[3] Buscar aluno')
    print('[4] Editar aluno')
    print('[5] Excluir aluno')
    print('[6] Estatísticas')
    print('[7] Sair')
    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        cadastrarAluno(alunos)
        print(alunos)
    elif opcao == 2:
        listarAlunos(alunos)
    elif opcao == 3:
        buscarAluno(alunos)
    elif opcao == 4:
        print('Editar aluno')
    elif opcao == 5:
        print('Excluir aluno')
    elif opcao == 6:
        print('estatisticas')
    elif opcao == 7:
        print('Saindo .', end= ' ')
        sleep(0.7)
        print('.', end= ' ')
        sleep(0.7)
        print('.', end= ' ')
        print('Até Logo!')
        break