"""Efetua import do(s) montador dos gráficos"""
from graph.factory.graphfactory import GraphFactory

h1 = "TÓPICOS ESPECIAIS"
title_div = "Dashboard para uma visualização (AC, ES, RN)"

"""Função que cria os gráficos"""


def plot_all_graph(mortalidade_graphs, neonatal_graphs, imunizacao_graphs):
    """Cria uma fábrica de gráficos"""
    graph_factory = GraphFactory(total_linhas=3, total_colunas=3)  # Inicializa a fábrica de gráficos
    graph_builder = graph_factory.get_graph("DASH", h1, title_div)  # Cria um contrutor de gráfico dash

    counter_coluna = 1
    """Plota a primeira linha com 3 gráficos"""
    for mortalidade_graph in mortalidade_graphs:
        if mortalidade_graph.serie_y2 is not None:
            graph_builder.plot_line_graph_different_scales(mortalidade_graph, linha=1, coluna=counter_coluna)
        else:
            graph_builder.plot_line_graph(mortalidade_graph, linha=1, coluna=counter_coluna)
        counter_coluna += 1

    """Plota o segundo gráfico"""
    counter_coluna = 1
    for neonatal_graph in neonatal_graphs:
        if neonatal_graph.serie_y2 is not None:
            graph_builder.plot_line_graph_different_scales(neonatal_graph, linha=2, coluna=counter_coluna)
        else:
            graph_builder.plot_line_graph(neonatal_graph, linha=2, coluna=counter_coluna)
        counter_coluna += 1

    counter_coluna = 1
    """Plota o terceiro gráfico"""
    for imunizacao_graph in imunizacao_graphs:
        if imunizacao_graph.serie_y2 is not None:
            graph_builder.plot_line_graph_different_scales(imunizacao_graph, linha=3, coluna=counter_coluna)
        else:
            graph_builder.plot_line_graph(imunizacao_graph, linha=3, coluna=counter_coluna)
        counter_coluna += 1

    graph_builder.show()


def plot_grouped_all_graph(mortalidade_graphs, neonatal_graphs, imunizacao_graphs):
    """Inicializa a fábrica de gráficos e Cria um contrutor de gráfico dash"""
    graph_builder = GraphFactory().get_graph("DASHGROUPED", h1, title_div)
    graph_builder.plot_line_graph_different_scales(mortalidade_graphs, "mortalidade_graphs",
                                                   mortalidade_graphs[0].title, mortalidade_graphs[0].ylabel,
                                                   mortalidade_graphs[0].y2label)

    graph_builder.plot_line_graph_different_scales(neonatal_graphs, "neonatal_graphs",
                                                   neonatal_graphs[0].title, neonatal_graphs[0].ylabel,
                                                   neonatal_graphs[0].y2label)

    graph_builder.plot_line_graph_different_scales(imunizacao_graphs, "imunizacao_graphs",
                                                   imunizacao_graphs[0].title, imunizacao_graphs[0].ylabel,
                                                   imunizacao_graphs[0].y2label)
    graph_builder.show()
