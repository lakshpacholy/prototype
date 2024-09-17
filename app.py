from dash import dcc, html, Dash
from dash.dependencies import Input, Output
from src.algorithms.route_calculator import calculate_sea_route, get_port_coordinates
from src.visualization.folium_map import create_map

# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[
    "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css",
    "/assets/custom.css"  
])

# Layout for the app
app.layout = html.Div([
    # Map Section
    html.Div([
        html.Iframe(
            id='folium-map',
            srcDoc=create_map('Mumbai', 'Chennai', get_port_coordinates)._repr_html_(),
            width='100%',
            height='100%',
            style={'border': 'none', 'position': 'absolute', 'top': 0, 'left': 0}
        ),
        html.Div([
            # Header Section
            html.Div([
                html.H1("Adaptive Ship Routing System", className='text-center mt-4 mb-4')
            ], className='overlay-header'),

            # Interactive Input Section
            html.Div([
                html.Label("Start Port:", className='mt-2'),
                dcc.Dropdown(
                    id='start-port',
                    options=[{'label': port, 'value': port} for port in ['Mumbai', 'Chennai', 'Kolkata', 'Goa', 'Delhi']],
                    value='Mumbai',
                    className='dropdown'
                ),

                html.Label("End Port:", className='mt-2'),
                dcc.Dropdown(
                    id='end-port',
                    options=[{'label': port, 'value': port} for port in ['Mumbai', 'Chennai', 'Kolkata', 'Goa', 'Delhi']],
                    value='Chennai',
                    className='dropdown'
                ),

                html.Button('Recalculate Route', id='button', n_clicks=0, className='btn btn-primary mt-2'),

                html.Div(id='route-distance', className='mt-2')
            ], className='overlay-controls'),

        ], className='overlay')
    ], className='map-container')
])

# Callback to update map, and route distance based on input
@app.callback(
    [Output('folium-map', 'srcDoc'),
     Output('route-distance', 'children')],
    [Input('button', 'n_clicks')],
    [Input('start-port', 'value'), Input('end-port', 'value')]
)
def update_content(n_clicks, start_port, end_port):

    # Update Folium map
    m = create_map(start_port, end_port, get_port_coordinates)
    map_html = m._repr_html_()

    # Calculate direct distance
    distance = calculate_sea_route(start_port, end_port)
    distance_text = f"Direct Distance: {distance:.2f} km" if distance != float('inf') else "Invalid ports specified"

    return  map_html, distance_text

if __name__ == '__main__':
    app.run_server(debug=True)
