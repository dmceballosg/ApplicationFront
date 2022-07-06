import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, State, Input

if __name__ == '__main__':
    app = dash.Dash()

    app.layout = html.Div([
        dcc.Input(id='name1', placeholder='Name 1', type='text', value=''),
        dcc.Input(id='name2', placeholder='Name 2', type='text', value=''),
        dcc.Input(id='lastname1', placeholder='LastName 1', type='text', value=''),
        dcc.Input(id='lastname2', placeholder='LastName 2', type='text', value=''),
        html.Button(id='submit-button', type='submit', children='Submit'),
        html.Div(id='output_div')
    ])

    def full_name(name1, name2, lastname1, lastname2):
        name = (name1 + ' ' + name2 + ' ' + lastname1 + ' ' + lastname2).upper()
        print(name)
        return name

    @app.callback(Output('output_div', 'children'),
                  [Input('submit-button', 'n_clicks')],
                  [State('username', 'value')],
                  )
    def update_output(clicks, name):
        if clicks is not None:
            print(clicks, name = full_name(name1, name2, lastname1, lastname2))

    app.run_server(host='0.0.0.0')
