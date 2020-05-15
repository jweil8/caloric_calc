import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, 
                   
    children=[
    html.H1(children='Caloric Needs Calculator'),

    html.Div(children='Welcome, I will need some information from you!'),
    
    html.Div(
        html.Div(children=[
            html.Label('Gender'),
            dcc.Dropdown(
                options=[
                    {'label': 'Male', 'value': 'M'},
                    {'label': 'Female', 'value': 'F'}
                ],
                value='M'
            ),

            html.Label('Height (Inches)'),
            dcc.Input(value='0', type='text'),

            html.Label('Weight (Pounds)'),
            dcc.Input(value='0', type='text')]),
             
         html.Div(children=[
            html.Label('Age (Years)'),
            dcc.Input(value='0', type='text'),

            html.Label('Activity Level'),
            dcc.Slider(
                min=0,
                max=5,
                marks={
                1: 'Sedentary',
                2: 'Lightly Active',
                3: 'Moderately Active',
                4: 'Very Active',
                5: 'Professionally Active'
            })]), 
        style={
                    'textAlign': 'left',
                    'color': colors['text'],
                    'columnCount': 2})
    ])

if __name__ == '__main__':
    app.run_server(debug=True)