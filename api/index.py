import dash
from dash import html

app = dash.Dash(__name__)
server = app.server  # required for Vercel

app.layout = html.Div([
    html.H1("Hello from Dash on Vercel!")
])
