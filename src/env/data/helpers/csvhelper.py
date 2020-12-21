"""Importa manipulador de CSV"""
import csv

"""Função para processar CSV em um dicionário de dados"""
def processar_csv_para_dicionario(caminho_arquivo, indice_coluna_chave, indice_coluna_valor):
    with open(caminho_arquivo, "r") as csv_file:  # Abre o csv com a finalização de recursos
        leitor_csv = csv.reader(csv_file, delimiter=';')  #Lê o csv pelo demilitador ";"
        quantidade_linhas = 0
        dic = {}  # Declara um dicionário
        for linha in leitor_csv:  # Percorre linha a linha do csv
            if quantidade_linhas == 0:  # Verifica se a linha não é cabeçalho
                quantidade_linhas += 1

            else: #Caso não adiciona ao dicionário
                dic[linha[indice_coluna_chave]] = linha[indice_coluna_valor]
                quantidade_linhas += 1
        return dic

"""Função para processar CSV em um dicionário de dados"""
def processar_csv_para_dicionario_lista_de_dados(caminho_arquivo, indice_coluna_chave, remover_index_coluna_chave = True):
    with open(caminho_arquivo, mode="r") as csv_file:  # Abre o csv com a finalização de recursos
        leitor_csv = csv.reader(csv_file, delimiter=';')  # Lê o csv pelo demilitador ";"
        quantidade_linhas = 0
        dic = {}  # Declara um dicionário
        list_header = []  # Declara uma lista de cabeçalhos
        for linha in leitor_csv:  # Percorre linha a linha do csv
            if quantidade_linhas == 0:
                if remover_index_coluna_chave:
                    del linha[indice_coluna_chave]  # Remove index da lista
                list_header = linha
            else:  # Linha não é cabeçalho
                valor_chave = linha[indice_coluna_chave]  # Cria a variável auxiliar para poder remover o index da lista
                if remover_index_coluna_chave:  # Verifica se o indíce deve passado deve ser removido
                    del linha[indice_coluna_chave]  # Remove index da lista
                """
                Cria um dicionário interno para associar ano e valor 
                para que seja possível filtrar todos os anos de interesse
                no pré processamento    
                """
                list_dados = []
                for indice in range(0, len(linha)):
                    list_dados.append({list_header[indice]: linha[indice]})
                dic[valor_chave] = list_dados.copy()  # Atribuí a lista ao dicionário
            quantidade_linhas += 1
        return dic