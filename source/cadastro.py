disciplinas_disponiveis = {
    1: 'Calculo 1',
    2: 'Matemática Discreta',
    3: 'Álgebra Linear e Geo Analítica',
    4: 'Programação Estruturada',
    5: 'Pensamento Computacional',
    6: 'Calculo 2',
    7: 'Desenvolvimento Web',
    8: 'Design Gráfico e User Experience',
    9: 'Métodos Ágeis de Dev. Software',
    10: 'Projeto de Ciência de Dados I',
    11: 'Matéria vaga'
}

alunos = {} # Dicionário para armazenar os alunos

def cadastrar_alunos():
    matricula = str(input('Matrícula: '))
    nome = input('Nome: ')
    semestre = input('Semestre: ')

    aluno = {
        'nome' : nome,
        'matricula' : matricula,
        'semestre' : semestre,
        'disciplinas' : {}
    }

    while True:
        print("\nEscolha uma disciplina:")
        for num, disciplina in disciplinas_disponiveis.items():
            print(f"{num}. {disciplina}")
        
        opcao = int(input("Digite o número da disciplina (ou '0' para finalizar): "))
        
        if opcao == 0:
            break
        elif opcao in disciplinas_disponiveis:
            nota = float(input(f"Digite a nota para {disciplinas_disponiveis[opcao]}: "))
            aluno['disciplinas'][disciplinas_disponiveis[opcao]] = nota
        else:
            print("Opção inválida. Tente novamente.")

    alunos[matricula] = aluno
    print(f"Aluno {nome} cadastrado com sucesso!")

def alterar_nota_aluno(matricula):
    if matricula in alunos:
        aluno = alunos[matricula]
        print(f"\nNotas atuais do aluno {aluno['nome']}:")
        
        # Mostrar as disciplinas com seus números
        for num, disciplina in disciplinas_disponiveis.items():
            if disciplina in aluno['disciplinas']:
                print(f"{num}. {disciplina}: {aluno['disciplinas'][disciplina]}")
        
        for i, materia in disciplinas_disponiveis.items():
            print (f'{materia} : {i}')
        # Escolher a disciplina pelo número
        opcao = int(input("\nDigite o número da disciplina que deseja alterar a nota: "))

        if opcao in disciplinas_disponiveis:
            disciplina_para_alterar = disciplinas_disponiveis[opcao]
            if disciplina_para_alterar in aluno['disciplinas']:
                nova_nota = float(input(f"Digite a nova nota para {disciplina_para_alterar}: "))
                aluno['disciplinas'][disciplina_para_alterar] = nova_nota
                print(f"Nota de {disciplina_para_alterar} alterada para {nova_nota}")
            else:
                print("Disciplina não encontrada no cadastro do aluno.")
        else:
            print("Número da disciplina inválido.")
    else:
        print("Aluno não encontrado.")

def calcular_media_aluno(matricula):
    if matricula in alunos:
        aluno = alunos[matricula]
        notas = [nota for nota in aluno['disciplinas'].values()]
        media = sum(notas) / len(notas)

        print(f"\nMédia geral do aluno {aluno['nome']}: {media:.2f}")
        
        if media >= 7:
            print("Aprovado")
        elif media < 4:
            print("Reprovado")
        else:
            print("Recuperação")
    else:
        print("Aluno não encontrado.")