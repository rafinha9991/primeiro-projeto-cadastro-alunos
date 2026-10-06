from time import sleep
def cadastrarAluno(alunos):
    nome = input('Digite o nome: ')
    idade = int(input('Idade: '))
    aluno = {'nome': nome,
             'idade': idade
             }
    alunos.append(aluno)

def listarAlunos(alunos):
    for aluno in alunos:
        print(f'{aluno['nome']} - {aluno['idade']}')

def buscarAluno(alunos):
    encontrou = False
    nome = input('Nome do aluno: ')
    for aluno in alunos:
        if nome == aluno['nome']:
            encontrou = True
            print('Aluno encontrado!')
            sleep(0.5)
            print(f'{aluno["nome"]} - {aluno["idade"]}')
    if not encontrou:
        print('Aluno não encontrado!')