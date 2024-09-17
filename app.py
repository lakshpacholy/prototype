from dash import dcc, html, Dash
from dash.dependencies import Input, Output
from src.algorithms.route_calculator import calculate_sea_route, get_port_coordinates
from src.visualization.folium_map import create_map
from src.visualization.plotly_charts import plot_fuel_vs_route

# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[
    "https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css",
    "/assets/custom.css"  # Custom CSS for additional styling
])

# Layout for the app
app.layout = html.Div([
    # Header Section
    html.Div([
        html.H1("Adaptive Ship Routing System", className='text-center mt-4 mb-4')
    ], className='container'),

    # Main Content Section
    html.Div([
        # Map Section
        html.Div([
            html.H3("Topographic Map", className='mb-3'),
            html.Iframe(id='folium-map',
                        srcDoc=create_map('Mumbai', 'Chennai', get_port_coordinates)._repr_html_(),
                        width='100%',
                        height='500',
                        style={'border': 'none'})
        ], className='col-md-12 mb-4'),

        # Plotly Chart Section
        html.Div([
            html.H3("Fuel Consumption vs Route Length", className='mb-3'),
            dcc.Graph(id='fuel-plot')
        ], className='col-md-12 mb-4'),

        # Interactive Input Section
        html.Div([
            html.Label("Start Port:", className='mt-2'),
            dcc.Dropdown(
                id='start-port',
                options=[{'label': port, 'value': port} for port in ['Mumbai', 'Chennai', 'Kolkata', 'Goa', 'Delhi']],
                value='Mumbai',
                className='mb-2'
            ),

            html.Label("End Port:", className='mt-2'),
            dcc.Dropdown(
                id='end-port',
                options=[{'label': port, 'value': port} for port in ['Mumbai', 'Chennai', 'Kolkata', 'Goa', 'Delhi']],
                value='Chennai',
                className='mb-2'
            ),

            html.Button('Recalculate Route', id='button', n_clicks=0, className='btn btn-primary mt-2'),

            html.Div(id='route-distance', className='mt-2')
        ], className='col-md-12 mt-4'),

    ], className='row container')

])

# Callback to update Plotly graph, map, and route distance based on input
@app.callback(
    [Output('fuel-plot', 'figure'),
     Output('folium-map', 'srcDoc'),
     Output('route-distance', 'children')],
    [Input('button', 'n_clicks')],
    [Input('start-port', 'value'), Input('end-port', 'value')]
)
def update_content(n_clicks, start_port, end_port):
    # Update Plotly graph
    fig = plot_fuel_vs_route()

    # Update Folium map
    m = create_map(start_port, end_port, get_port_coordinates)
    map_html = m._repr_html_()

    # Calculate direct distance
    distance = calculate_sea_route(start_port, end_port)
    distance_text = f"Direct Distance: {distance:.2f} km" if distance != float('inf') else "Invalid ports specified"

    return fig, map_html, distance_text

if __name__ == '__main__':
    app.run_server(debug=True)
