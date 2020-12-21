
"""Converte valores de um dicionário com uma lista de dicionário de string para float"""
def conversor_dados_string_float(lista_valores):
    lista_valores_float = []
    for dic in lista_valores:
       for chave_ano in dic:
           valor_preprocessado = dic[chave_ano].replace(",", ".").replace("%", "")
           lista_valores_float.append({chave_ano: float(valor_preprocessado)})
    return lista_valores_float

"""Método que filtra e converte dicionário em lista de valores"""
def filtra_converte_dicionario_em_lista(lista_filtro, lista_valores):
    serie = []
    for dic in lista_valores:
        for chave in dic:
            if str(chave) in lista_filtro:
                serie.append(dic[chave])
    return serie

"""Método que filtra e converte dicionário de dados em série"""
def filtra_converte_dicionario_para_serie(dic_valores, codigo_uf, lista_ano):
    lista_valores = dic_valores[codigo_uf]
    lista_valores_float = conversor_dados_string_float(lista_valores)
    lista_ano_str = []
    [(lista_ano_str.append(str(ano))) for ano in lista_ano]
    serie = filtra_converte_dicionario_em_lista(lista_ano_str, lista_valores_float)
    return serie

"""Método que cria matriz com objetos"""
def cria_matriz_com_objetos(total_linhas, total_colunas, obj):
    lista = []
    for i in range(0, total_linhas):
        colunas = []
        for j in range(0, total_colunas):
            colunas.append(obj)
        lista.append(colunas)
    return lista

"""Método que cria lista com objetos"""
def cria_lista_com_objetos(total_linhas, obj):
    lista = []
    for i in range(0, total_linhas):
        lista.append(obj)
    return lista