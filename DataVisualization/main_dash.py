# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import dash
import plotly.express as px
import pandas as pd

app = Dash(__name__)
df = pd.DataFrame(
    {
        "Fruits": ["Apple", "Banana", "Orange", "Apple", "Banana", "Orange"],
        "Amount": [4, 3, 1, 2, 2, 1],
        "City": ["New York City", "New York City", "New York City", "Montreal", "Montreal", "Montreal"]
    }
)
multi_select = dcc.Dropdown(
    id='multi-select-dropdown',
    options=[{'label': i, 'value': i} for i in df['Fruits'].unique()],
    value=['Apple', 'Orange'],
    multi=True
)

@app.callback(
    dash.dependencies.Output('pie-chart', 'figure'),
    [dash.dependencies.Input('multi-select-dropdown', 'value')]
)
def update_pie_chart(selected_fruits):
    filtered_df = df[df['Fruits'].isin(selected_fruits)]
    fig = px.pie(filtered_df, values='Amount', names='Fruits', title='Fruit Consumption per City')
    return fig

fig = px.pie(df, values='Amount', names='Fruits', title='Fruit Consumption per City')

app.layout = html.Div([
    html.Div(children=[

        html.Br(),
        html.Label('Multi-Select Dropdown'),
        multi_select,

        html.Br(),
        html.Label('Radio Items'),
        dcc.RadioItems(['New York City', 'Montréal', 'San Francisco'], 'Montréal'),
    ], style={'padding': 10, 'flex': 1}),

    html.Div(children=[
        html.Label('Checkboxes'),
        dcc.Checklist(['New York City', 'Montréal', 'San Francisco'],
                      ['Montréal', 'San Francisco']
        ),

        html.Br(),
        html.Label('Text Input'),
        dcc.Input(value='MTL', type='text'),

        html.Br(),
        html.Label('Slider'),
        dcc.Slider(
            min=0,
            max=9,
            marks={i: f'Label {i}' if i == 1 else str(i) for i in range(1, 6)},
            value=5,
        ),

        html.Br(),
        html.Label('Pie Chart'),
        dcc.Graph(figure=fig, id='pie-chart')
    ], style={'padding': 10, 'flex': 1})
], style={'display': 'flex', 'flexDirection': 'row'})

if __name__ == '__main__':
    app.run(debug=True)
