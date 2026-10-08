from time import sleep
def cadastrarAluno(alunos):
    nome = input('Digite o nome: ')
    idade = int(input('Idade: '))
    aluno = {'nome': nome,
             'idade': idade
             }
    alunos.append(aluno)
    print('Adicionando aluno.', end = ' ')
    sleep(0.6)
    print('.', end = ' ')
    sleep(0.6)
    print('.', end = ' ')
    sleep(0.6)
    print('\033[32mAluno adicionado com sucesso!\033[m')

def listarAlunos(alunos):
    for aluno in alunos:
        print(f'{aluno['nome']} - {aluno['idade']}')

def buscarAluno(alunos):
    while True:
        encontrou = False
        nome = input('Nome do aluno: ')
        for aluno in alunos:
            if nome == aluno['nome']:
                encontrou = True
                print('\033[32mAluno encontrado!\033[m')
                sleep(0.5)
                print(f'{aluno["nome"]} - {aluno["idade"]}')
                return aluno
        if not encontrou:
            print('\033[1;31mAluno não encontrado!\033[m')
            print('\033[33mDigite o nome novamente.')

def editarAluno(alunos):
    aluno = buscarAluno(alunos)

    while True:
        if aluno:
            escolha = input('Qual caracteristica deseja mudar?[B=ambos/N=nome/I=idade]: ').strip().upper()[0]
            if escolha not in 'BNI':
                print('\033[1;31mOpçao inválida! Digite B ou N ou I.\033[m')

            elif escolha == 'B':
                while True:
                    novoNome = input('Digite um novo nome: ').strip()

                    if not novoNome.replace(' ','').isalpha():
                        print('\033[1;31mDigite apenas letras!\033[m')
                    else:
                        break
                while True:
                    try:
                        novaIdade = int(input('Digite uma nova idade: '))
                        break
                    except ValueError:
                        print('\033[1;31mDigite apenas número!\033[m')

                aluno['nome'] = novoNome
                aluno['idade'] = novaIdade
                print('Modificado com sucesso!')
                sleep(1)
                break

            elif escolha == 'N':
                novoNome = input('Digite um novo nome: ').strip()

                if not novoNome.replace(' ', '').isalpha():
                    print('\033[1;31mDigite apenas letras!\033[m')
                else:
                    break
                aluno['nome'] = novoNome
                print('Modificado com sucesso!')
                sleep(1)
                break

            elif escolha == 'I':
                while True:
                    try:
                        novaIdade = int(input('Digite uma nova idade: '))
                        break
                    except ValueError:
                        print('\033[1;31mDigite apenas número!\033[m')
                aluno['idade'] = novaIdade
                print('Modificado com sucesso!')
                sleep(1)
                break

def excluirAlunos(alunos):
    aluno = buscarAluno(alunos)

    while True:
        if aluno:
            remover = input('Remover esse aluno?[S/N]: ').strip().upper()[0]
            if remover not in 'SN':
                print('\033[1;31mOpçao inválida! Digite S ou N\033[m')
            elif remover == 'S':
                alunos.remove(aluno)
                print('Removendo aluno.', end = ' ')
                sleep(0.6)
                print('.', end=' ')
                sleep(0.6)
                print('.', end=' ')
                sleep(0.6)
                print('Aluno removido com sucesso!')
                break
            elif remover == 'N':
                print('voltando...')
                sleep(1)
                break
def estatisticasAlunos(alunos):
    