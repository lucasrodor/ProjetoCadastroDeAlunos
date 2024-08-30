import pandas as pd
import os
from openpyxl import load_workbook

import pandas as pd
import os

def carregar_dados_existentes(arquivo_excel):
    if os.path.exists(arquivo_excel):
        return pd.read_excel(arquivo_excel, engine='openpyxl')
    return pd.DataFrame(columns=['Matrícula', 'Nome', 'Semestre', 'Disciplina', 'Nota'])

def salvar_alunos_excel(arquivo_excel, alunos):
    # Carrega os dados existentes
    df_existente = carregar_dados_existentes(arquivo_excel)

    # Converte os dados dos alunos para um DataFrame
    dados_alunos = []
    for matricula, info_aluno in alunos.items():
        for disciplina, nota in info_aluno['disciplinas'].items():
            dados_alunos.append({
                'Matrícula': matricula,
                'Nome': info_aluno['nome'],
                'Semestre': info_aluno['semestre'],
                'Disciplina': disciplina,
                'Nota': nota
            })

    df_novos_dados = pd.DataFrame(dados_alunos)

    # Junta os dados existentes com os novos dados
    df_atualizado = pd.concat([df_existente, df_novos_dados], ignore_index=True)

    # Remove duplicatas
    df_atualizado = df_atualizado.drop_duplicates(subset=['Matrícula', 'Disciplina'])

    # Tranforma a matrícula para string
    df_atualizado['Matrícula'] = df_atualizado['Matrícula'].astype(str)

    # Salva os dados atualizados de volta no arquivo Excel
    df_atualizado.to_excel(arquivo_excel, index=False, engine='openpyxl')

    # Ajusta a largura das colunas para melhor organização
    ajustar_largura_colunas(arquivo_excel)

    print(f"Dados salvos em {arquivo_excel}")

def abrir_planilha_excel(caminho_arquivo):
    os.startfile(caminho_arquivo)

def ajustar_largura_colunas(arquivo_excel):
    # Carrega o arquivo Excel
    workbook = load_workbook(arquivo_excel)
    sheet = workbook.active

    # Ajusta a largura das colunas com base no conteúdo
    for column in sheet.columns:
        max_length = 0
        column_letter = column[0].column_letter  # Pega a letra da coluna
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = (max_length + 2)  # Adiciona um pequeno buffer
        sheet.column_dimensions[column_letter].width = adjusted_width

    # Salva o arquivo com as novas larguras de coluna
    workbook.save(arquivo_excel)

def limpar_planilha_excel(arquivo_excel):
    # Verifica se o arquivo existe
    if os.path.exists(arquivo_excel):
        # Cria um DataFrame vazio com as colunas esperadas
        df_vazio = pd.DataFrame(columns=['Matrícula', 'Nome', 'Semestre', 'Disciplina', 'Nota'])
        
        # Salva o DataFrame vazio no arquivo Excel, sobrescrevendo o existente
        df_vazio.to_excel(arquivo_excel, index=False, engine='openpyxl')
        
        print(f"A planilha {arquivo_excel} foi limpa com sucesso.")
    else:
        print(f"O arquivo {arquivo_excel} não existe.")