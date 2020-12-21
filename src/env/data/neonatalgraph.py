from data.helpers.datahelper import lista_dados_anos
from helpers import listhelper
from data.helpers import dataextractionhelper, csvhelper
from data.helpers.processadadoshelper import processa_dados_idh
from models.graph import Graph

"""função que monta o modelo gráfico"""
def build(UF):
    serie_x = lista_dados_anos()
    title = "IDH X Taxa de Cesáreos total"
    codigo_uf = dataextractionhelper.retorna_codigo_uf(UF)
    serie_y = processa_dados_idh(codigo_uf, serie_x)
    serie_y2 = processa_dados_cesareos(codigo_uf, serie_x)
    grafico = Graph(title, serie_x, serie_y, serie_y2, "Anos", "IDH", "Cesareos", uf=UF)
    return grafico

"""Retorna a lista de valores de idh no respectivo código uf"""
def processa_dados_cesareos(codigo_uf, lista_ano):
    caminho_arquivo = dataextractionhelper.caminho_arquivo_partos_cesareos_csv()  # Retorna o caminho do arquivo csv contendo o idh
    dic_valores = csvhelper.processar_csv_para_dicionario_lista_de_dados(caminho_arquivo, 0)
    return listhelper.filtra_converte_dicionario_para_serie(dic_valores, codigo_uf, lista_ano)