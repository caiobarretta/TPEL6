"""
Classe modelo para os gráficos
"""
class Graph:
    """Contrutor da classe"""
    def __init__(self, title, serie_x, serie_y, serie_y2=None, xlabel='', ylabel='', y2label='', uf=''):
        self.title = title

        self.serie_x = serie_x
        self.serie_y = serie_y
        self.serie_y2 = serie_y2

        self.xlabel = xlabel
        self.ylabel = ylabel
        self.y2label = y2label

        self.uf = uf