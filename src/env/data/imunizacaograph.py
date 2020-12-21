from data.helpers.datahelper import lista_dados_anos
from helpers import listhelper
from data.helpers import dataextractionhelper, csvhelper
from models.graph import Graph


"""função que monta o modelo gráfico"""
def build(UF):
    serie_x = lista_dados_anos()
    title = "Imunização X Mortalidade Tardia"  # Título do gráfico
    codigo_uf = dataextractionhelper.retorna_codigo_uf(UF)
    serie_y = processa_dados_imunizacao(codigo_uf, serie_x)
    serie_y2 = processa_dados_mortalidade_tardia(codigo_uf, serie_x)
    grafico = Graph(title, serie_x, serie_y, serie_y2, "Anos", "Imunização", "Mortalidade Tardia", uf=UF)
    return grafico

"""Retorna a lista de valores da mortalidade no respectivo código uf"""
def processa_dados_imunizacao(codigo_uf, lista_ano):
    caminho_arquivo = dataextractionhelper.caminho_arquivo_imunizacoes_csv()  # Retorna o caminho do arquivo csv contendo a mortalidade
    dic_valores = csvhelper.processar_csv_para_dicionario_lista_de_dados(caminho_arquivo, 0)
    return listhelper.filtra_converte_dicionario_para_serie(dic_valores, codigo_uf, lista_ano)

"""Retorna a lista de valores da mortalidade no respectivo código uf"""
def processa_dados_mortalidade_tardia(codigo_uf, lista_ano):
    caminho_arquivo = dataextractionhelper.caminho_arquivo_mortalidade_tardia_csv()  # Retorna o caminho do arquivo csv contendo a mortalidade
    dic_valores = csvhelper.processar_csv_para_dicionario_lista_de_dados(caminho_arquivo, 0)
    return listhelper.filtra_converte_dicionario_para_serie(dic_valores, codigo_uf, lista_ano)