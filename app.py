import dash
from dash import Dash, html, dcc, Output, Input, State, callback

app = Dash(__name__,
           suppress_callback_exceptions=True)

app.layout = html.Div([
    html.H1('TFT Dashboard'),
        html.Div(dcc.Input(id='input-on-submit', type='text')),
    html.Button('Submit', id='submit_val', n_clicks=0),
    html.Div(id='container-button-basic',
             children='Enter a value and press submit')
])

def get_data(data:str) -> str:
    """
    Test function for callback and method chanining

    Args:
        data (str): str input to test

    Returns:
        str: modified input
    """
    return f"summoner_id: {data}"

@callback(
    Output('container-button-basic', 'children'),
    Input('submit_val', 'n_clicks'),
    State('input-on-submit', 'value'),
    prevent_initial_call=True
)
def update_output(n_clicks, value):
    return 'The input value was {} and the button has been clicked {} times'.format(
        get_data(value),
        n_clicks
    )


if __name__ == '__main__':
    app.run(debug=True)
