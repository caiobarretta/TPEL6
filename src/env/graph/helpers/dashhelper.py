"""Seta o encoding para utf-8"""
# -*- coding: utf-8 -*-

"""Efetua o importa da bilioteca para plotar os gráficos"""
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.figure_factory as ff

"""Efetua importa da biblioteca json"""
import json

"""Função que cria um gráfico"""
def build_app():
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    return app

"""Função que cria um eixo para o  gráfico"""
def build_axis(name, data_axis_x, data_axis_y, yaxis="y"):
    return go.Scatter(
        x=data_axis_x,
        y=data_axis_y,
        name=name,
        yaxis=yaxis
    )

"""Função que cria uma figura para grafico de linhas"""
def build_figure_linear_graph_different_scales(title, yaxis_title, yaxis2_title, data_yaxis, data_yaxis2):
    return {'data': [data_yaxis, data_yaxis2], 'layout': go.Layout(
        title=title,
        yaxis=dict(title=yaxis_title),
        yaxis2=dict(
            title=yaxis2_title,
            titlefont=dict(color='rgb(148, 103, 189)'),
            tickfont=dict(color='rgb(148, 103, 189)'),
            overlaying='y',
            side='right'
        )
    )}

"""Função que cria uma figura para grafico de linha com diferentes escalas"""
def build_figure_linear_graph(title, yaxis_title, data_yaxis):
    return {'data': [data_yaxis], 'layout': go.Layout(
        title=title,
        yaxis=dict(title=yaxis_title)
    )}

"""Teste gráfico histograma com distplot"""
def build_figure_histogram_distplot(hist_data, group_labels):
    return ff.create_distplot(hist_data, group_labels)

"""Função que cria um layout de um gráfico de diferentes escalas"""
def build_graph(id_graph, figure, class_name):
    return html.Div(children=[
        dcc.Graph(id=id_graph, figure=figure)
    ], className=class_name)

"""Função que cria título principal"""
def build_title_main(h1, title_div):
    return html.Div(children=[
        html.H1(children=h1),
        html.Div(children=title_div)
    ])

"""Função que cria dropdown layout"""
def build_drop_down(graphs_dropdown, id_dropdown, total_colunas):
    options = []
    selected_values = []
    graphs_dropdown_filter = graphs_dropdown[(total_colunas*id_dropdown):(total_colunas+(3*id_dropdown))]
    for graph in graphs_dropdown_filter:
        value_dict = {"id": graph["id"], "linha": (graph["linha"]-1), "coluna": (graph["coluna"]-1), "graph_type": graph["graph_type"]}
        value = json.dumps(value_dict)
        options.append({"label": graph["title"], "value": value})
        selected_values.append(value)

    return html.Div([
        dcc.Dropdown(
            id='dropdown-{}'.format(id_dropdown),
            options=options,
            value=selected_values,
            multi=True,
            placeholder="Selecione o gráfico",
        )
    ])

"""Retorna o nome da classe da div pela quantidade de colunas"""
def get_class_name_by_column(total_colunas):
    if total_colunas == 1:
        return "twelve columns"
    elif total_colunas == 2:
        return "six columns"
    elif total_colunas == 3:  # Como a classe column tem um padding-left de 4% não é possível usar 4 colunas corretamente
        return "three columns"
    elif total_colunas == 4:
        return "three columns"
    elif total_colunas == 6:
        return "two columns"
    else:
        return "one column"

"""Função que cria o layout principal a partir de uma lista de layouts"""
def build_layout_main(layouts, total_linhas, total_colunas, dropdown):
    list_layout_main = [layouts[0]]  # Lista principa do programa
    list_dropdown = []  # Lista de drop downs

    if dropdown:  # Adiociona drop down
        for dropdown_layout in layouts[1]:  # Percorre a lista de drop downs
            list_dropdown.append(dropdown_layout)
        divs = layouts[2]
    else:
        divs = layouts[1]

    count_dropdown = 0
    count_iteractions_append = 0
    for linha in range(0, total_linhas):
        list_div_graph = []
        if dropdown:
            list_layout_main.append(
                html.Div(list_dropdown[linha], id="layout-graphs-{}".format(count_dropdown), className="row"))
        for coluna in range(0, total_colunas):
            div = divs[linha][coluna]
            if div is not None and div not in list_div_graph:
                list_div_graph.append(div)
                list_layout_main.append(div)
                count_iteractions_append += 1
        count_dropdown += 1
    return html.Div(list_layout_main, id="layout-main", className="row")

"""Função que cria o layout principal a partir de uma lista de layouts"""
def build_grouped_layout_main(layouts):
    return html.Div(layouts, id="layout-main", className="row")

"""Função que recria o layout dos gráficos"""
def rebuild_graphs(layouts, total_linhas, colunas):
    list_layout = []
    divs = layouts[2]
    for linha in range(0, total_linhas):
        for coluna in colunas:
            list_layout.append(divs[linha][coluna])
    return html.Div(list_layout, id="layout-graphs", className="row")