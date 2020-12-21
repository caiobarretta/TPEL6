from helpers import listhelper
from data.helpers import dataextractionhelper, csvhelper

"""Retorna a lista de valores de idh no respectivo código uf"""
def processa_dados_idh(codigo_uf, lista_ano):
    caminho_arquivo = dataextractionhelper.caminho_arquivo_idh_csv()  # Retorna o caminho do arquivo csv contendo o idh
    dic_valores = csvhelper.processar_csv_para_dicionario_lista_de_dados(caminho_arquivo, 0)
    return listhelper.filtra_converte_dicionario_para_serie(dic_valores, codigo_uf, lista_ano)