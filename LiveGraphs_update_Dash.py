import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as  html
import plotly
import random
import plotly.graph_objs as pgo
from collections import deque

X= deque(maxlen= 10)
Y= deque(maxlen= 10)
#To get some initial starting data
X.append(1)
Y.append(1)

app= dash.Dash(__name__)
#Html of the entire project
#children referring to the actual content & dcc component to get the HTML of input & output fields
app.layout = html.Div(children=[
    dcc.Graph(id= 'live-graph', animate= True),
    dcc.Interval(id= 'graph-update',
                 interval= 1000,
                 n_intervals= 0)
                
])

#decorator to update the graph in real-time with events
@app.callback(
    Output(component_id= 'live-graph', component_property= 'figure'),
    [Input('graph-update', 'n_intervals')]
)
def update_graph(input_data):
    global X
    global Y
    X.append(X[-1]+1)
    Y.append(Y[-1]+(Y[-1]*random.uniform(-0.1, 0.1)))
#passing the data of the graph   
    data= pgo.Scatter(
        x= list(X),
        y= list(Y),
        name= 'Scatter-plot'
    )
    return {'data': [data],
            'layout': pgo.Layout(xaxis= dict(range= [min(X), max(X)]),
                                 yaxis= dict(range= [min(Y), max(Y)]))}
#Run the application
if __name__ == "__main__":
    app.run_server(debug=True)