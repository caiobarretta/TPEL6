"""Efetua import do(s) helper(s) para auxiliar a montagem dos gráficos"""
from helpers import listhelper
from graph.helpers import dashhelper

import dash

"""Efetua importa da biblioteca json"""
import json

class DashGraph:

    """Construtor que cria o app"""
    def __init__(self, h1, title_div, total_linhas=1, total_colunas=1, dropdown=False):
        self.app = dashhelper.build_app()  # Chama ajudante para criar app dash
        self.total_linhas = total_linhas
        self.total_colunas = total_colunas
        self.layouts = []
        self.graphs_dropdown = []
        self.counter = 1
        self.dropdown = dropdown

        lista_matriz_vazia = listhelper.cria_matriz_com_objetos(total_linhas, total_colunas, None)
        div_title_main = dashhelper.build_title_main(h1, title_div)
        self.layouts.append(div_title_main)
        if dropdown:
            lista_vazia_drop_down = []
            for linha in range(0, total_linhas):
                lista_vazia_drop_down.append(None)
            self.layouts.append(lista_vazia_drop_down)
        self.layouts.append(lista_matriz_vazia)

    """Função que plota gráfico de linha de diferentes escalas"""
    def plot_line_graph_different_scales(self, graph, linha=1, coluna=1, id_graph=None):
        data1 = dashhelper.build_axis(graph.ylabel, graph.serie_x, graph.serie_y)
        data2 = dashhelper.build_axis(graph.y2label, graph.serie_x, graph.serie_y2, "y2")
        figure = dashhelper.build_figure_linear_graph_different_scales(graph.title, graph.ylabel,
                                                                       graph.y2label, data1, data2)
        if id_graph is None:
            id_graph = "line-graph-different-scales-{}".format(self.counter)
        self.create_graph_layout(graph, linha, coluna, figure, id_graph, "line_graph_different_scales")

    """Função que plota gráfico de linha"""
    def plot_line_graph(self, graph, linha=1, coluna=1, id_graph=None):
        data = dashhelper.build_axis(graph.ylabel, graph.serie_x, graph.serie_y)
        figure = dashhelper.build_figure_linear_graph(graph.title, graph.ylabel, data)

        if id_graph is None:
            id_graph = "line-graph{}-".format(self.counter)
        self.create_graph_layout(graph, linha, coluna, figure, id_graph, "line_graph")

    """Função que plota gráfico histograma"""
    def plot_histogram_graph(self, graph, linha=1, coluna=1, id_graph=None):
        data = graph.serie_x
        hist_data = [data]
        group_labels = [graph.ylabel]
        figure = dashhelper.build_figure_histogram_distplot(hist_data, group_labels)
        self.create_graph_layout(graph, linha, coluna, figure, id_graph, "density_graph")

    """Cria a div que contém o gráfico"""
    def create_graph_layout(self, graph, linha, coluna, figure, id_graph, graph_type):
        class_name = dashhelper.get_class_name_by_column(self.total_colunas)

        """Adiciona um gráfico em uma lista de gráficos"""
        self.graphs_dropdown.append({"id": self.counter, "title": graph.title, "linha": linha, "coluna": coluna, "graph_type": graph_type, "graph": graph})

        div = dashhelper.build_graph(id_graph, figure, class_name)
        if self.dropdown:
            divs = self.layouts[2]
        else:
            divs = self.layouts[1]

        divs[linha-1][coluna-1] = div
        self.counter += 1

    """Redimensiona cada gráfico"""
    def resize_graph_layout(self, linha, coluna, graph_type, graph):
        self.counter += 1
        if graph_type == "line_graph_different_scales":
            self.plot_line_graph_different_scales(graph, linha, coluna)
        elif graph_type == "line_graph_different_scales":
            self.plot_line_graph(graph, linha, coluna)
        elif graph_type == "density_graph":
            self.plot_histogram_graph(graph, linha, coluna)

    def rebuild_graphs(self, values):
        list_coluna = []
        list_linha = []
        """Novo total de colunas para recalcular o tamanho dos gráficos"""
        novo_total_colunas = 0
        for value in values:
            novo_total_colunas += 1
        self.total_colunas = novo_total_colunas

        for value in values:
            value_dict = json.loads(value)
            coluna = value_dict["coluna"] + 1
            linha = value_dict["linha"] + 1
            graph_type = value_dict["graph_type"]
            id = value_dict["id"]

            graph = None
            for dict in self.graphs_dropdown:
                if dict["id"] == id:
                    graph = dict["graph"]

            if graph is not None:
                self.resize_graph_layout(linha, coluna, graph_type, graph)
            list_coluna.append(coluna - 1)
            list_linha.append(linha - 1)

        return list_coluna, list_linha

    """Construtor que exibe o app"""
    def show(self, debug=True):
        if self.dropdown:
            list_dropdown = self.layouts[1]
            list_dropdown_criado = []
            dropdown_counter = 0
            for dropdown in list_dropdown:
                div_dropdown = dashhelper.build_drop_down(self.graphs_dropdown, dropdown_counter, self.total_colunas)
                list_dropdown_criado.append(div_dropdown)
                dropdown_counter += 1
            self.layouts[1] = list_dropdown_criado
        """Constrói o layout principal atráves do helper"""
        self.app.layout = dashhelper.build_layout_main(self.layouts, self.total_linhas, self.total_colunas, self.dropdown)

        if self.dropdown:
            dropdown_counter = 0
            for dropdown in list_dropdown:
                """Função de callback para pegar retorno do drop down que atualiza os gráficos"""
                @self.app.callback(dash.dependencies.Output('layout-graphs-{}'.format(dropdown_counter), 'children'), [dash.dependencies.Input('dropdown-{}'.format(dropdown_counter), 'value')])
                def update_output(values):
                    raise NotImplementedError("To be implemented")
                dropdown_counter += 1

        """Inicializa o servidor"""
        self.app.run_server(debug=debug)
