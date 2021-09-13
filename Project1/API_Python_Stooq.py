import dash
import  dash_core_components as dcc
import dash_html_components as html
import  plotly.graph_objects as go
from dash.dependencies import Output,Input,State


external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css']

app=dash.Dash(__name__,external_stylesheets=external_stylesheets)

# some example company names
markdown="""

More information on website [Stooq](https://stooq.pl/) 

|Symbol  |Company name |
|--------|--------|
|AAPL    |Apple  |
|NFLX    |Netflix|
|CDR     |CD Projekt SA| 
|TSLA    |Tesla    | 
|AMZN    |Amazon    | 
"""
#creating application layout
app.layout=html.Div([
    html.H3('Share price of individual companies'),

    html.Div(
        dcc.Input(id='stock_input',value='AAPL',type='text',placeholder='Enter the company symbol...'),

    ),
    html.Button(id='submit-button',n_clicks=0,children='Load data'),

    html.Div(
        dcc.Graph(id='graph_close')),

    html.Hr(),

    html.Div([
        dcc.Markdown(markdown)])
])

@app.callback(Output('graph_close','figure'),
            [Input('submit-button','n_clicks')],
            [State('stock_input','value')])

def update_graph(n_clicks,input_value):
    def financial_data(n_clicks,company=input_value):
        """
        Function to download data from website
        """
        import pandas_datareader as web
        return web.DataReader(name=company, data_source='stooq')

    df = financial_data(n_clicks)
    df = df.reset_index()
    data=[]
    value_stock = go.Candlestick(x=df.Date,
                            open=df.Open,
                            high= df.High,
                            low=df.Low,
                            close=df.Close,
                            visible=True,
                            showlegend=False,
                            name='Stocks')

    data.append(value_stock)
    # creating timestamp selector
    layout=dict(title=input_value,
                xaxis=dict(
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
    )




    return {
            'data':data,
            'layout':layout
             }


if __name__=='__main__':
    app.run_server(debug=True,port=8049)
