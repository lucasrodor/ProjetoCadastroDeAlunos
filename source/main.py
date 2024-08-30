from cadastro import cadastrar_alunos, alunos, alterar_nota_aluno, calcular_media_aluno
from excel_handler import salvar_alunos_excel, abrir_planilha_excel, limpar_planilha_excel
from plotter import gerar_grafico_notas
import os 


if __name__ == "__main__":
    while True:
        print("\n1. Cadastrar aluno")
        print("2. Salvar Alunos na planilha")
        print("3. Verificar média e situação")
        print("4. Gerar gráfico de notas")
        print("5. Alterar nota de aluno")
        print("6. Limpar dados ")
        print("7. Abrir planilha")
        print("8. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            cadastrar_alunos()
        elif escolha == '2':
            salvar_alunos_excel('data/students.xlsx', alunos)
            caminho_absoluto = os.path.abspath('data/students.xlsx')
            if os.path.exists(caminho_absoluto):
                abrir_planilha_excel(caminho_absoluto)
            else:
                print(f"Arquivo não encontrado: {caminho_absoluto}")
        elif escolha == '3':
            matricula = input('Digite a matrícula do aluno:')
            calcular_media_aluno(matricula)
        elif escolha == '4':
            matricula = input("Digite a matrícula do aluno para gerar o gráfico: ")
            gerar_grafico_notas(alunos, matricula)
        elif escolha == '5':
            matricula = input("Digite a matrícula do aluno para alterar a nota: ")
            alterar_nota_aluno(matricula)
        elif escolha =='6':
            certeza = input('Tem certeza que deseja apagar os dados? (S/N)').upper().strip()
            if certeza == 'S':
                limpar_planilha_excel('data/students.xlsx')
            else:
                continue
        elif escolha == '7':
            caminho_absoluto = os.path.abspath('data/students.xlsx')
            if os.path.exists(caminho_absoluto):
                abrir_planilha_excel(caminho_absoluto)
            else:
                print(f"Arquivo não encontrado: {caminho_absoluto}")
        elif escolha == '8':
            print(alunos)
            print('-'*20)
            print ('PROGARMA FINALIZADO')

            break
        else:
            print("Opção inválida!")