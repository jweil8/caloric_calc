import pandas as pd
import numpy as np


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import chart_studio.plotly as py
import plotly.graph_objects as go


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}



app.layout = html.Div([
    html.Div(
        [html.H2(children='Caloric Need Dashboard'),
        html.H5(children='Welcome, I will need some information from you!')],
        style={"textAlign": "center", 
                'backgroundColor': colors['background'], 
                'color': colors['text']}),
    html.Div([
            html.Label('Gender'),
            dcc.Dropdown(
                id='gender',
                options=[
                    {'label': 'Male', 'value': 'M'},
                    {'label': 'Female', 'value': 'F'}
                ],
                value='M'),

            html.Label('Height (in)'),
            dcc.Input(id='ht', value='0', type='text'),

            html.Label('Weight (lbs)'),
            dcc.Input(id='wt', value='0', type='text'),
            
            html.Label('Age (years)'),
            dcc.Input(id='age', value='0', type='text')],
        style={ 'backgroundColor': colors['background'], 
                'textAlign': 'left',
                'color': colors['text'],
                'columnCount': 2}),

        html.Div([html.Label('Activity Level'),
            dcc.Slider(
                id='alevel',
                min=0,
                max=6,
                value=1,
                marks={
                1: 'Sedentary',
                2: 'Lightly Active',
                3: 'Moderately Active',
                4: 'Very Active',
                5: 'Professionally Active'})],
                 
            
                 style={'textAlign': 'center', 
                        'backgroundColor': colors['background'], 
                        'textAlign': 'left', 
                        'color': colors['text'], 
                        'width': '100%', 
                        'margin-left': 'auto', 
                        'margin-right': 'auto'}),
    
        html.Div(html.Table([
                    html.Tr([html.Td(['Basal Metabloic Rate (BMR)']), html.Td(id='bmr'), html.Td(title=('The number of calories you"d burn if you stayed in bed all day'))]),
                    html.Tr([html.Td(['Total Daily Energy Expenditure (TDEE)']), html.Td(id='tdee'), html.Td(title=('A measure of how many calories you burn per day'))])
        ]),
                style={'textAlign': 'center',
                           'margin-left': 'auto', 
                           'margin-right': 'auto'})
])    

@app.callback(
    [Output('bmr', 'children'),
     Output('tdee', 'children')],
    [Input('gender', 'value'),
     Input('ht', 'value'),
     Input('wt', 'value'),
     Input('age', 'value'),
     Input('alevel', 'value')
    ])
def both(gender, ht, wt, age, alevel):
        if gender == 'M':
            BMR = 66 + (6.23 * float(wt)) + (12.7 * float(ht)) - (6.8 * float(age))
        else:
            BMR = 655 + (4.35 * float(wt)) + (4.7 * float(ht)) - (4.7 * float(age))

        if alevel == 1:
            tdee = BMR*1.2

        elif alevel == 2:
            tdee = BMR*1.375

        elif alevel == 3:
            tdee = BMR*1.55

        elif alevel == 4:
            tdee = BMR*1.725

        elif alevel == 5:
            tdee = BMR*1.9

        return (int(BMR), int(tdee))

if __name__ == '__main__':
    app.run_server(debug=True)