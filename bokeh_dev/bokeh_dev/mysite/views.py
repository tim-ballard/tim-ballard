from django.shortcuts import render
from bokeh.models import ColumnDataSource
from bokeh.transform import dodge
from bokeh.plotting import figure
from bokeh.embed import components

# Create your views here.
def homepage(request):

    fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
    years = ['2015', '2016', '2017']

    data = {'fruits' : fruits,
            '2015'   : [2, 1, 4, 3, 2, 4],
            '2016'   : [5, 3, 3, 2, 4, 6],
            '2017'   : [3, 2, 4, 4, 5, 3]}

    source = ColumnDataSource(data=data)

    p = figure(x_range=fruits, y_range=(0, 10), height=250, title="Fruit counts by year",
            toolbar_location=None, tools="")

    p.vbar(x=dodge('fruits', -0.25, range=p.x_range), top='2015', width=0.2, source=source,
        color="#c9d9d3", legend_label="2015")

    p.vbar(x=dodge('fruits',  0.0,  range=p.x_range), top='2016', width=0.2, source=source,
        color="#718dbf", legend_label="2016")

    p.vbar(x=dodge('fruits',  0.25, range=p.x_range), top='2017', width=0.2, source=source,
        color="#e84d60", legend_label="2017")

    p.x_range.range_padding = 0.1
    p.xgrid.grid_line_color = None
    p.legend.location = "top_left"
    p.legend.orientation = "horizontal"

    #store
    script, div = components(p)

    #return to django
    return render(request, 'pages/base.html', {'script': script, 'div': div})