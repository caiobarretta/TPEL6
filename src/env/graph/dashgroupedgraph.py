import json

from plotly.subplots import make_subplots

from graph.helpers import dashhelper

"""Efetua o importa da bilioteca para plotar os gráficos"""
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.figure_factory as ff


class DashGroupedGraph:
    """Construtor que cria o app"""

    def __init__(self, h1, title_div, total_linhas=1, total_colunas=1, dropdown=False):
        self.app = dashhelper.build_app()  # Chama ajudante para criar app dash
        self.layouts = []
        self.list_graph_dict = []
        self.counter = 1
        div_title_main = dashhelper.build_title_main(h1, title_div)
        self.layouts.append(div_title_main)

    def plot_line_graph_different_scales(self, graphs, id_graph, title, ylabel, y2label, tem_drop_down=True,
                                         rebuild=False):
        # Cria uma figura com eixo y sencundário
        figure = make_subplots(specs=[[{"secondary_y": True}]])

        for graph in graphs:
            """adiciona linhas"""
            figure.add_trace(go.Scatter(x=graph.serie_x, y=graph.serie_y, name=graph.ylabel + " - " + graph.uf),
                             secondary_y=False, )
            figure.add_trace(go.Scatter(x=graph.serie_x, y=graph.serie_y2, name=graph.y2label + " - " + graph.uf),
                             secondary_y=True, )

        figure.update_layout(title_text=title)  # Adiciona título na figura
        figure.update_xaxes(title_text=ylabel)  # Atribui título no eixo x
        figure.update_yaxes(title_text="<b>" + ylabel + "</b>", secondary_y=False)  # Atribui títulos ao eixos-y
        figure.update_yaxes(title_text="<b>" + y2label + "</b>", secondary_y=True)  # Atribui títulos ao eixos-y2

        class_name = dashhelper.get_class_name_by_column(1)
        id_div_graph = "div-{}".format(id_graph)

        div_children = html.Div(children=[
            dcc.Graph(id=id_graph, figure=figure)
        ], className=class_name)

        div = html.Div(children=[div_children], id=id_div_graph)

        if rebuild:
            return div_children

        if tem_drop_down:
            drop_down_name = 'dropdown-{}'.format(id_graph)
            options = []
            selected_values = []

            for graph in graphs:
                indentifier_graph = id_graph + "-" + graph.uf
                self.list_graph_dict.append({indentifier_graph: {"id_graph": id_graph, "graph": graph,
                                                                 "type_graph": "graph_different_scales",
                                                                 "title": title, "ylabel": ylabel, "y2label": y2label}})
                options.append({"label": graph.uf, "value": indentifier_graph})
                selected_values.append(indentifier_graph)

            div_drop_down = html.Div([
                dcc.Dropdown(
                    id=drop_down_name,
                    options=options,
                    value=selected_values,
                    multi=True,
                    placeholder="Selecione a UF",
                )])
            self.layouts.append(
                {"drop_down": div_drop_down, "id_drop_down": drop_down_name, "id_div": id_div_graph, "div": div})
        else:
            self.layouts.append(
                {"id_div": id_div_graph, "div": div})

    """Verifica o tipo do gráfico e retorna a div filha atráves do método de plotagem correspondente"""
    def rebuild_graph(self, graphs, id_graph, title, ylabel, y2label, type_graph):
        if type_graph == "graph_different_scales":
            return self.plot_line_graph_different_scales(graphs, id_graph, title, ylabel, y2label, False, True)

    def show(self, debug=True):
        list_layout_to_build = []
        for dic_layout in self.layouts:
            if "drop_down" in dic_layout:
                div_drop_down = dic_layout["drop_down"]
                list_layout_to_build.append(div_drop_down)

            if "div" in dic_layout:
                div = dic_layout["div"]
                list_layout_to_build.append(div)

        self.app.layout = dashhelper.build_grouped_layout_main(list_layout_to_build)
        for dic_layout in self.layouts:
            if "drop_down" in dic_layout and "div" in dic_layout:
                @self.app.callback(dash.dependencies.Output(dic_layout["id_div"], 'children'),
                                   [dash.dependencies.Input(dic_layout["id_drop_down"], 'value')])
                def update_output(values):
                    list_graph, id_graph, title, ylabel, y2label, type_graph = [], "", "", "", "", ""
                    for value in values:
                        dict_graph = None
                        for graph_dict in self.list_graph_dict:
                            if value in graph_dict:
                                dict_graph = graph_dict[value]

                        if dict_graph is not None:
                            id_graph, title, ylabel = dict_graph["id_graph"], dict_graph["title"], dict_graph["ylabel"]
                            y2label, type_graph = dict_graph["y2label"], dict_graph["type_graph"]
                            list_graph.append(dict_graph["graph"])
                    if len(list_graph) > 0:
                        return self.rebuild_graph(list_graph, id_graph, title, ylabel, y2label, type_graph)

        """Inicializa o servidor"""
        self.app.run_server(debug=debug)
