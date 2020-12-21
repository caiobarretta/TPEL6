"""Importa as chamadas do sistema operacional"""
import os

"""Importa o ajudante de processamento de csv"""
from data.helpers import csvhelper

caminho_relativo_preprocessamento = "/Data-Source/preprocess/"
caminho_relativo_arquivo_codigo_uf_csv = caminho_relativo_preprocessamento + "Codigo-UF.csv"

caminho_relativo_arquivo_idh_csv = caminho_relativo_preprocessamento + "mortalidade_graph/Indice de Desenvolvimento Humano - 2000, 2010-2015.csv"
caminho_relativo_mortalidade_csv = caminho_relativo_preprocessamento + "mortalidade_graph/Neonatal Total Taxa de Mortalidade Neonatal Total 2000-2016.csv"

caminho_relativo_partos_cesareos_csv = caminho_relativo_preprocessamento + "neonatal_graph/Proporção de Partos Cesáreos.csv"

caminho_relativo_imunizacoes_csv = caminho_relativo_preprocessamento + "imunizacao_graph/Imunizações 2000-2016.csv"
caminho_relativo_mortalidade_tardia_csv = caminho_relativo_preprocessamento + "imunizacao_graph/Taxa de mortalidade 7 a 27 dias - 2000-2016.csv"

"""Método que retorna o endereco da pasta que contém os código da uf no formato csv"""
def caminho_arquivo_codigo_uf_csv():
    caminho = retorna_caminho(2)
    """Monta o caminho completo do arquivo de código uf"""
    return caminho + caminho_relativo_arquivo_codigo_uf_csv

"""Método que retorna o endereco da pasta que contém IDH no formato csv"""
def caminho_arquivo_idh_csv():
    caminho = retorna_caminho(2)
    """Monta o caminho completo do arquivo de código uf"""
    return caminho + caminho_relativo_arquivo_idh_csv

"""Método que retorna o endereco da pasta que contém a Mortalidade no formato csv"""
def caminho_arquivo_mortalidade_csv():
    caminho = retorna_caminho(2)
    """Monta o caminho completo do arquivo de mortalidade"""
    return caminho + caminho_relativo_mortalidade_csv

"""Método que retorna o endereco da pasta que contém a Partos cesareos no formato csv"""
def caminho_arquivo_partos_cesareos_csv():
    caminho = retorna_caminho(2)
    """Monta o caminho completo do arquivo de partos cesareos"""
    return caminho + caminho_relativo_partos_cesareos_csv

"""Método que retorna o endereco da pasta que contém a Imunizações no formato csv"""
def caminho_arquivo_imunizacoes_csv():
    caminho = retorna_caminho(2)
    """Monta o caminho completo do arquivo de Imunizações"""
    return caminho + caminho_relativo_imunizacoes_csv

"""Método que retorna o endereco da pasta que contém a mortalidade tardia no formato csv"""
def caminho_arquivo_mortalidade_tardia_csv():
    caminho = retorna_caminho(2)
    """Monta o caminho completo do arquivo de Mortalidade tardia"""
    return caminho + caminho_relativo_mortalidade_tardia_csv

"""Método que retorna um caminho de arquivo n vezes"""
def retorna_caminho(n):
    """Recupera o caminho atual"""
    caminho = os.getcwd()
    for x in range(0, n):
        """Retorna o caminho n vezes no projeto independente de sistema operacional"""
        caminho = os.path.normpath(caminho + os.sep + os.pardir)
    return caminho

"""Método que retorn o codigo da UF do arquivo csv"""
def retorna_codigo_uf(UF):
    caminho_arquivo_csv = caminho_arquivo_codigo_uf_csv()  #  Retorna o caminho do arquivo de código uf csv
    dic = csvhelper.processar_csv_para_dicionario(caminho_arquivo_csv, 1, 0)  # Converte csv para dicionario
    if(UF not in dic):
        """Lança um erro indicando que a UF não está no arquivo csv"""
        raise NameError("A UF: {} não foi encontrado no arquivo: {}".format(UF, caminho_arquivo_codigo_uf_csv))
    return dic[UF]