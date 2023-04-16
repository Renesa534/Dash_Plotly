import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as  html
import pandas_datareader.data as web
import datetime


start= datetime.datetime(2018, 1, 1)
end= datetime.datetime.now()

#bring the stock info
stock= 'TSLA'
df= web.DataReader(stock, 'quandl', start, end, access_key= 'r6wdDaKqVY9UVaPVd9pY')
app= dash.Dash()
#Html of the entire project
#children referring to the actual content & Plotly Graph component used via dcc
app.layout = html.Div(children=[
    html.Div(children= '''
   Financial Data'''),
            dcc.Input(id= 'input', value= '', type= 'text'),
            html.Div(id= 'output-graph')])

@app.callback(
    Output(component_id= 'output-graph', component_property= 'children'),
    [Input(component_id= 'input', component_property= 'value')]
)

def update_graph(input_data):
    start= datetime.datetime(2018, 1, 1)
    end= datetime.datetime.now()
    #bring the stock info
    df= web.DataReader(input_data, 'quandl', start, end, api_key= 'r6wdDaKqVY9UVaPVd9pY')
    df.reset_index(inplace= True)
    df.set_index('Date', inplace= True)
    return dcc.Graph(id='example-graph',
                figure={'data': [{'x':df.index, 'y':df.Close, 'type':'line', 'name': stock}],
                        'layout': {
                           'title': 'Stock'
                                                   }})

#Run the application
if __name__ == "__main__":
    app.run_server(debug=True)
