from time import sleep
from funcoes.interface.interface import *
from funcoes.arquivo.arquivo import *
alunos = list()

while True:
    sleep(1.3)
    cabecalho('SISTEMA DE ALUNOS')
    print('[1] Cadastrar novo aluno')
    print('[2] Listar alunos')
    print('[3] Buscar aluno')
    print('[4] Editar aluno')
    print('[5] Excluir aluno')
    print('[6] Estatísticas')
    print('[7] Sair')
    try:
        opcao = int(input('Escolha uma opção: '))
    except ValueError:
        print('\033[1;31mDigite apenas números!\033[m') #"\033[m" dar cores, 1 = negrito, 31 = vermelho
        continue

    if opcao == 1:
        cadastrarAluno(alunos)
    elif opcao == 2:
        listarAlunos(alunos)
    elif opcao == 3:
        buscarAluno(alunos)
    elif opcao == 4:
        editarAluno(alunos)
    elif opcao == 5:
        excluirAlunos(alunos)
    elif opcao == 6:
        estatisticasAlunos(alunos)
    elif opcao == 7:
        print('Saindo .', end= ' ')
        sleep(0.7)
        print('.', end= ' ')
        sleep(0.7)
        print('.', end= ' ')
        print('Até Logo!')
        break