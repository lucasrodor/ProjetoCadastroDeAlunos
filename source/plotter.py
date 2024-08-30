import matplotlib.pyplot as plt

def gerar_grafico_notas(alunos, matricula):
    if matricula in alunos:
        aluno = alunos[matricula]
        disciplinas = list(aluno['disciplinas'].keys())
        notas = list(aluno['disciplinas'].values())

        plt.bar(disciplinas, notas)
        plt.xlabel('Disciplinas')
        plt.ylabel('Notas')
        plt.title(f'Notas de {aluno["nome"]}')
        plt.show()
    else:
        print("Aluno não encontrado!")