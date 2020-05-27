import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}



app.layout = html.Div(
                   
    children=[
    html.H2(children='Caloric Need Dashboard'),

    html.H5(children='Welcome, I will need some information from you!'),
    
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

            html.Label('Height (in)'),
            dcc.Input(value='0', type='text'),

            html.Label('Weight (lbs)'),
            dcc.Input(value='0', type='text'),
            
            html.Label('Age (years)'),
            dcc.Input(value='0', type='text'),

            html.Label('Activity Level'),
            dcc.Slider(
                min=0,
                max=5,
                value=1,
                marks={
                1: 'Sedentary',
                2: 'Lightly Active',
                3: 'Moderately Active',
                4: 'Very Active',
                5: 'Professionally Active'})]
                )
            )], 
        
        style={     
                'backgroundColor': colors['background'], 
                'textAlign': 'left',
                'color': colors['text'],
                'columnCount': 2})
    
def bmr(gender, wt, ht, age):
    if gender == 'Male':
        BMR = (10 * (wt*2.2)) + (6.25*(ht*0.39)) -(5*age) + 5
    else:
        BMR = (10 * (wt*2.2)) + (6.25*(ht*0.39)) - (5*age) - 161
    return BMR

def h_b(BMR,act_lvl):
    
    if act_lvl == 1:
        daly_need = BMR*1.2
        
    elif act_lvl == 2:
        daly_need = BMR*1.375
        
    elif act_lvl == 3:
        daly_need = BMR*1.55
        
    elif act_lvl == 4:
        daly_need = BMR*1.725
        
    elif act_lvl == 5:
        daly_need = BMR*1.9
        
    return daly_need

if __name__ == '__main__':
    app.run_server(debug=True)