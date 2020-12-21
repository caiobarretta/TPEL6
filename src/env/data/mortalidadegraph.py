"""Importa a class Graph do arquivo graph"""
from data.helpers.datahelper import lista_dados_anos
from data.helpers.processadadoshelper import processa_dados_idh
from models.graph import Graph

"""Importa o ajudante de extração de dados,  csv e lista"""
from helpers import listhelper
from data.helpers import dataextractionhelper, csvhelper


#função que monta o modelo gráfico
def build(UF):
    serie_x = lista_dados_anos()
    title = "IDH X Taxa de Mortalidade"  # Título do gráfico
    codigo_uf = dataextractionhelper.retorna_codigo_uf(UF)  # Retorna Código UF
    serie_y = processa_dados_idh(codigo_uf, serie_x)
    serie_y2 = processa_dados_mortalidade(codigo_uf, serie_x)

    grafico = Graph(title, serie_x, serie_y, serie_y2, "Anos", "IDH", "Mortalidade", uf=UF)
    return grafico  # Retorna o gráfico

"""Retorna a lista de valores da mortalidade no respectivo código uf"""
def processa_dados_mortalidade(codigo_uf, lista_ano):
    caminho_arquivo = dataextractionhelper.caminho_arquivo_mortalidade_csv()  # Retorna o caminho do arquivo csv contendo a mortalidade
    dic_valores = csvhelper.processar_csv_para_dicionario_lista_de_dados(caminho_arquivo, 0)
    return listhelper.filtra_converte_dicionario_para_serie(dic_valores, codigo_uf, lista_ano)