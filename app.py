from dash import dcc, html, Dash
from dash.dependencies import Input, Output
from src.algorithms.route_calculator import calculate_sea_route, get_port_coordinates
from src.visualization.folium_map import create_map

app = Dash(__name__, external_stylesheets=[
    "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css",
    "/assets/custom.css"
])

app.layout = html.Div([
    html.Div([
        html.Iframe(
            id='folium-map',
            srcDoc=create_map('Mumbai', 'Chennai', get_port_coordinates)._repr_html_(),
            width='100%',
            height='100%',
            style={'border': 'none', 'position': 'absolute', 'top': 0, 'left': 0}
        ),
        html.Div([
            html.H1("Adaptive Ship Routing System", className='text-center mt-4 mb-4'),
            html.Label("Start Port:", className='mt-2'),
            dcc.Dropdown(
                id='start-port',
                options=[{'label': port, 'value': port} for port in ['Mumbai', 'Chennai', 'Kolkata', 'Goa', 'Dighi Port']],
                value='Mumbai',
                className='dropdown'
            ),
            html.Label("End Port:", className='mt-2'),
            dcc.Dropdown(
                id='end-port',
                options=[{'label': port, 'value': port} for port in ['Mumbai', 'Chennai', 'Kolkata', 'Goa', 'Dighi Port']],
                value='Chennai',
                className='dropdown'
            ),
            html.Button('Recalculate Route', id='button', n_clicks=0, className='btn btn-primary mt-2'),
            html.Div(id='route-distance', className='mt-2')
        ], className='overlay-controls')
    ], className='map-container')
])

@app.callback(
    [Output('folium-map', 'srcDoc'),
     Output('route-distance', 'children')],
    [Input('button', 'n_clicks')],
    [Input('start-port', 'value'), Input('end-port', 'value')]
)
def update_content(n_clicks, start_port, end_port):
    m = create_map(start_port, end_port, get_port_coordinates)
    map_html = m._repr_html_()
    distance_info = calculate_sea_route(start_port, end_port)
    distance = distance_info.get('direct_distance_km', float('inf'))
    distance_text = f"Direct Distance: {distance:.2f} km" if distance != float('inf') else "Invalid ports specified"
    return map_html, distance_text

if __name__ == '__main__':
    app.run_server(debug=True)
