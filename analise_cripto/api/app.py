from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import requests
import pandas as pd
import os


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


btc_df = pd.read_csv(os.path.join(os.path.dirname(__file__), '../data/raw/coin_Bitcoin.csv'))
eos_df = pd.read_csv(os.path.join(os.path.dirname(__file__), '../data/raw/coin_EOS.csv'))
sol_df = pd.read_csv(os.path.join(os.path.dirname(__file__), '../data/raw/coin_Solana.csv'))


app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("Dashboard de Previsão de Criptomoedas", className="text-center mb-4"), width=12)
    ]),
    
    dbc.Row([
        dbc.Col([
            html.Label("Selecione a Criptomoeda:"),
            dcc.Dropdown(
                id='crypto-dropdown',
                options=[
                    {'label': 'Bitcoin', 'value': 'BTC'},
                    {'label': 'EOS', 'value': 'EOS'},
                    {'label': 'Solana', 'value': 'SOL'}
                ],
                value='BTC',
                clearable=False
            )
        ], width=4)
    ]),
    
    dbc.Row([
        dbc.Col(dcc.Graph(id='prediction-chart'), width=12)
    ]),
    
    dbc.Row([
        dbc.Col(html.Div(id='prediction-output', className="mt-4"), width=12)  # Exibe a previsão da API
    ])
])

# Callback para obter previsões da API
@app.callback(
    Output('prediction-output', 'children'),
    [Input('crypto-dropdown', 'value')]
)
def get_predictions(selected_crypto):
    url = f"http://api:5000/predict?crypto={selected_crypto}"
    try:
        response = requests.get(url)
        print(f"Request feito para URL: {url}")
        
        if response.status_code == 200:
            prediction = response.json()
            print(f"Resposta da API: {prediction}")  # Log da resposta da API
            return f'Previsão para {selected_crypto}: {prediction["forecast"]}'
        else:
            print(f"Erro na resposta da API: {response.status_code}")
            return "Erro ao obter a previsão"
    except requests.exceptions.RequestException as e:
        print(f"Erro durante a chamada da API: {e}")
        return "Erro ao conectar com a API"

# Callback para atualizar o gráfico de previsão
@app.callback(
    Output('prediction-chart', 'figure'),
    [Input('crypto-dropdown', 'value')]
)
def update_prediction_chart(selected_crypto):
    # Seleciona o dataframe baseado na criptomoeda escolhida
    if selected_crypto == 'BTC':
        df = btc_df
    elif selected_crypto == 'EOS':
        df = eos_df
    else:
        df = sol_df


    if 'Predicted_Close' in df.columns:
        fig = px.line(df, x='Date', y=['Close', 'Predicted_Close'], 
                      title=f'Preço Real vs Previsão - {selected_crypto}')
    else:
        fig = px.line(df, x='Date', y='Close', title=f'Preço de Fechamento - {selected_crypto}')
    
    fig.update_layout(transition_duration=500)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')
