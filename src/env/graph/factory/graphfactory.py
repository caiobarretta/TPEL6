"""Classe que 'fabrica' os gráficos"""
from graph.dashgraph import DashGraph
from graph.dashgroupedgraph import DashGroupedGraph


class GraphFactory:

    """Construtor que cria os objetos da fábrica"""
    def __init__(self, total_linhas=1, total_colunas=1):
        self._graphs = {}
        self.register_type_graph("DASH", DashGraph)
        self.register_type_graph("DASHGROUPED", DashGroupedGraph)
        self.total_linhas = total_linhas
        self.total_colunas = total_colunas

    """Método que registra o tipo de gráfico no dicionário de gráficos"""
    def register_type_graph(self, type_graph, creator):
        self._graphs[type_graph] = creator

    """Método que retorna o gráfico pela chave do dicionário"""
    def get_graph(self, type_graph, h1, title_div):
        graph = self._graphs.get(type_graph)
        if not graph:
            raise ValueError(type_graph)
        return graph(h1, title_div, self.total_linhas, self.total_colunas)

