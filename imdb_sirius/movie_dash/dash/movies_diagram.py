from dash import html, dcc, no_update
from django_plotly_dash import DjangoDash
import plotly.graph_objects as go
from movies.models import Movie, Director, Type, OriginalName
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State
from django.db.models import Count

app = DjangoDash('MovieDiagram')
layout_dropdown = [{'label': 'Типы', 'value': 'type'}, {'label': 'Режиссеры', 'value': 'director'}]
app.layout = html.Div(
    [html.H1('Диаграмма режиссеров'),
    dcc.Graph(
        id='movies_diagram'
    ),
    dbc.Button(id='update_diagram', children='Обнови Диаграмму', n_clicks=0),
    dcc.Dropdown(id='dropdown_diagram', options=layout_dropdown)]
)



@app.callback(
    Output('movies_diagram', 'figure'),
    Input('update_diagram', 'n_clicks'),
    Input('dropdown_diagram', 'value')
)
def update_movie_diagram(n, value):
    if value == 'director':
        directors_movies_count = Director.objects.all().values('name').annotate(movies_count=Count('movie'))
    elif value == 'type':
        directors_movies_count = Type.objects.all().values('name').annotate(movies_count=Count('movie'))
    else:
        return no_update
    data = go.Pie(
        values=[director['movies_count'] for director in directors_movies_count],
        labels=[director['name'] for director in directors_movies_count]
    )
    layout = {
        'showlegend': True
    }
    return go.Figure(data=data, layout=layout)
