"""Seta o encoding para utf-8"""
# -*- coding: utf-8 -*-
from helpers.plotterhelper import plot_all_graph, plot_grouped_all_graph

""" Efetua o import dos gráficos"""
from data import imunizacaograph, mortalidadegraph, neonatalgraph

"""Função Principal"""
def main():
    list_uf = ["AC", "ES", "RN"]
    mortalidade_graphs = []
    imunizacao_graphs = []
    neonatal_graphs = []
    for uf in list_uf:
        mortalidade_graphs.append(mortalidadegraph.build(uf))  # Monta o gráfico de mortalidade para cada uf
        neonatal_graphs.append(neonatalgraph.build(uf))  # Monta o gráfico de natalidade para cada uf
        imunizacao_graphs.append(imunizacaograph.build(uf))  # Monta o gráfico de natalidade para cada uf

    """Plota os gráficos"""
    #plot_all_graph(mortalidade_graphs, neonatal_graphs, imunizacao_graphs)
    plot_grouped_all_graph(mortalidade_graphs, neonatal_graphs, imunizacao_graphs)

if __name__ == '__main__':
    main()
