key = ***********************

import quandl
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

quandl.ApiConfig.api_key = key

# Load Data

df = quandl.get("WSE/PKOBP")
df = df.reset_index()

# First Plot

# Create figure
fig = go.Figure()

fig.add_trace(
    go.Scatter(x=list(df.Date), y=list(df.Open)))

# Set title
fig.update_layout(
    title_text="Kurs otwarcia"
)
# creating time slider
range_slider = dict(
    rangeselector=dict(
        buttons=list([
            dict(count=1,
                 label="1m",
                 step='month',
                 stepmode="backward"),
            dict(count=3,
                 label="3m",
                 step="month",
                 stepmode="backward"),
            dict(count=6,
                 label="6m",
                 step="month",
                 stepmode="backward"),
            dict(count=1,
                 label="1Y",
                 step="year",
                 stepmode="backward"),
            dict(count=3,
                 label="3Y",
                 step="year",
                 stepmode="backward"),
            dict(step="all")
        ])
    ),
    rangeslider=dict(
        visible=False
    ),
    type="date"
)

# Add range slider
fig.update_layout(
    xaxis=range_slider
)
# Second Plot

# Create figure
fig2 = go.Figure()

fig2.add_trace(
    go.Scatter(x=list(df.Date), y=list(df.Close)))

# Set title
fig2.update_layout(
    title_text="Kurs zamknięcia"
)

# Add range slider
fig2.update_layout(
    xaxis=range_slider
)
# Third Plot

# Create figure
fig3 = go.Figure()

fig3.add_trace(
    go.Scatter(x=list(df.Date), y=list(df.High)))

# Set title
fig3.update_layout(
    title_text="Najwyższe notowania danego dnia"
)

# Add range slider
fig3.update_layout(
    xaxis=range_slider
)
# Four Plot

# Create figure
fig4 = go.Figure()

fig4.add_trace(
    go.Scatter(x=list(df.Date), y=list(df.Low)))

# Set title
fig4.update_layout(
    title_text="Najniższe notowania danego dnia"
)

# Add range slider
fig4.update_layout(
    xaxis=range_slider
)
# Last Plot

# Create figure
fig5 = go.Figure()

fig5.add_trace(
    go.Bar(x=list(df.Date), y=list(df.Volume)))

# Set title
fig5.update_layout(
    title_text="Wartość volumenu"
)

# Add range slider
fig5.update_layout(
    xaxis=range_slider
)

app.layout = html.Div([
    html.H3('Notowania akcji banku PKO BP'),
    html.H6('Waluta - PLN'),
    dcc.Graph(figure=fig),
    dcc.Graph(figure=fig2),
    dcc.Graph(figure=fig3),
    dcc.Graph(figure=fig4),
    dcc.Graph(figure=fig5)
])

if __name__ == '__main__':
    app.run_server(debug=True, port=8045)
