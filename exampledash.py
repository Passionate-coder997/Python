import dash
import dash_core_components as dcc
import dash_html_components as html
import webbrowser

app=dash.Dash()

def main():
    global app
    colors={
        'background':'#111111',
        'text':'#456FBF'
    }
    webbrowser.open_new('http://127.0.0.1:5060/')
    app.layout = html.Div(style={'backgroundcolor':colors['background']},children=[
        html.H1(
            children='Hello Dash',
            style={
                'textAlign':'center',
                'color':colors['text']
            }
        ),
        html.Div(children='Dash a web application framework in python', 
     style={
            'textAlign':'center',
            'color':colors['text']
        }),
        dcc.Graph(
            id='Sample_graph',
            figure={
                'data':[
                    {'x':[1,2,3,4], 'y':[4,2,1], 'type':'bar', 'name':'SG'},
                    {'x':[1,2,3,4], 'y':[4,2,1], 'type':'bar', 'name': u'Montreal'},
                ],
                'layout':{
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor':colors['background'],
                    'font':{
                        'color':colors['text']
                    }
                }
            }
        )
    ])
    app.run_server(port=5060)
if __name__=='__main__':
    main()