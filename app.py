import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify
from dash.dependencies import Input, Output
from src.algorithms.route_calculator import calculate_sea_route, get_port_coordinates
from src.visualization.folium_map import create_map

# Initialize the Dash app with a Bootstrap theme
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MORPH])
app.title = "Matsya Navigation"  # Tab Title

# Example data (these would come from your backend or API)
ship_data = {
    "latitude": 37.7749,
    "longitude": -122.4194,
    "speed": 15,  # in knots
    "course": 180,  # in degrees
    "waypoints": [
        {"lat": 38.5, "lon": -123.0, "name": "Waypoint 1"},
        {"lat": 36.5, "lon": -121.0, "name": "Waypoint 2"},
    ],
    "weather": {
        "temperature": 20,
        "wind_speed": 12,
        "condition": "Clear"
    },
    "alerts": ["Engine check required", "Storm ahead"],
}

# Global card styling
CARD_STYLE = {
    "border-radius": "15px",
    "box-shadow": "0 6px 12px rgba(0, 0, 0, 0.1)",
    "transition": "0.3s ease-in-out",
    "padding": "20px",
    "margin": "15px",
    "background-color": "#fdfdfd",
}

# Hamburger menu (Off-canvas component)
offcanvas = dbc.Offcanvas(
    [
        html.H5("Matsya Navigation", className="text-center text-light", style={"font-size": "28px"}),  # Change title color to light and increase size
        html.P("Pioneers of ship navigation", className="text-center text-light", style={"font-size": "14px", "margin-top": "5px"}),  # Subtitle
        html.Hr(className="bg-dark"),  # Dark horizontal rule for contrast
        dbc.Nav(
            [
                dbc.NavLink("Home", href="#", active="exact", className="text-dark"),
                dbc.NavLink("Map", href="#ship-position-map", className="text-dark"),
                dbc.NavLink("Waypoints", href="#waypoints-section", className="text-dark"),
                dbc.NavLink("Settings", href="#settings", className="text-dark"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    id="offcanvas-menu",
    title="",  # Leave title empty since it's included in the content
    is_open=False,
    style={
        "width": "350px",
        "background-color": "black",  # Dark background
        "color": "#ffffff",  # Set default text color to white
        "padding": "20px",  # Add padding for better spacing
        "border-radius": "5px",  # Optional: Rounded corners
    },
)



# Layout for the Dash app
app.layout = dbc.Container(
    fluid=True,
    style={"background-color": "#f7f8fa", "padding": "30px"},
    children=[
        # Offcanvas component
        offcanvas,

        # Header Section with Logo
        dbc.Row(
            dbc.Col(
                html.Div(
                    className="d-flex align-items-center justify-content-center",
                    style={"position": "relative"},
                    children=[
                        # Fish Logo
                        html.Img(
                            src="https://cdn-icons-png.flaticon.com/512/4197/4197736.png",  # Fish icon URL
                            style={"height": "100px", "margin-right": "20px"}
                        ),
                        html.H1(
                            "Matsya Navigation",
                            className="text-center text-light p-4",
                            style={
                                "border-radius": "10px",
                                "box-shadow": "0px 4px 8px rgba(0,0,0,0.1)",
                                "width": "100%",
                                "font-size": "48px",
                                "background-color": "black",  # Set background to black
                            },
                        ),
                        dbc.Button(
                            DashIconify(icon="fa-solid:bars", width=30, color="white"),
                            id="open-offcanvas",
                            className="ms-2",
                            style={
                                "background-color": "transparent",
                                "border": "none",
                                "position": "absolute",  # Ensure it stays in place
                                "right": "30px",  # Adjust to make it more visible
                            }
                        ),

                    ],
                ),
                width=12,
            ),
        ),

        # Brief Description
        dbc.Row(
            dbc.Col(
                html.P(
                    "This dashboard provides real-time information on the ship's current location, speed, weather, "
                    "and alerts. The path of the ship and upcoming waypoints are also displayed for better navigation.",
                    className="text-center",
                    style={"font-size": "18px", "margin-bottom": "30px", "color": "#555"}
                ),
                width=12,
            )
        ),
        
        # Ship Information Section
        dbc.Row(
            [
                # Ship Position Card
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardBody(
                                [
                                    html.H4("Ship Position", className="card-title"),
                                    html.Div(
                                        [
                                            DashIconify(icon="fa6-solid:map-marker-alt", width=24, color="red"),
                                            html.Span(f" Latitude: {ship_data['latitude']}"),
                                            html.Br(),
                                            DashIconify(icon="fa6-solid:map-marker-alt", width=24, color="blue"),
                                            html.Span(f" Longitude: {ship_data['longitude']}"),
                                        ],
                                        className="d-flex align-items-center",
                                        style={"font-size": "18px"}
                                    ),
                                    html.Hr(),
                                    dcc.Graph(
                                        id="ship-position-map",
                                        figure={
                                            "data": [
                                                dict(
                                                    type="scattermapbox",
                                                    lat=[ship_data['latitude']],
                                                    lon=[ship_data['longitude']],
                                                    mode="markers",
                                                    marker=dict(size=14, color="red"),
                                                    text=["Current Position"]
                                                )
                                            ],
                                            "layout": dict(
                                                mapbox=dict(
                                                    style="open-street-map",
                                                    center={"lat": ship_data['latitude'], "lon": ship_data['longitude']},
                                                    zoom=10
                                                ),
                                                height=300,
                                                margin={"l": 0, "r": 0, "t": 0, "b": 0},
                                                paper_bgcolor="rgba(0, 0, 0, 0)",
                                            )
                                        },
                                    )
                                ]
                            ),
                        ],
                        style=CARD_STYLE,
                    ),
                    width=6
                ),
                # Speed & Course Card
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H4("Speed & Course", className="card-title"),
                                dbc.Row(
                                    [
                                        dbc.Col(
                                            dbc.Card(
                                                [
                                                    html.H5(
                                                        [DashIconify(icon="fa-solid:tachometer-alt", width=24),
                                                         " Speed"], className="card-subtitle mb-2"),
                                                    html.H1(f"{ship_data['speed']} knots", className="text-primary"),
                                                ],
                                                body=True,
                                                style={"text-align": "center", "border-color": "#007bff", "padding": "10px"}
                                            ),
                                        ),
                                        dbc.Col(
                                            dbc.Card(
                                                [
                                                    html.H5(
                                                        [DashIconify(icon="fa-solid:compass", width=24),
                                                         " Course"], className="card-subtitle mb-2"),
                                                    html.H1(f"{ship_data['course']}°", className="text-success"),
                                                ],
                                                body=True,
                                                style={"text-align": "center", "border-color": "#28a745", "padding": "10px"}
                                            ),
                                        )
                                    ]
                                )
                            ]
                        ),
                        style=CARD_STYLE,
                    ),
                    width=6
                ),
            ]
        ),
        
        # Input Start and End Points Section
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        [
                            # Title
                            html.H4(
                                [DashIconify(icon="fa-solid:map-signs", width=24), " Set Start & End Points"],
                                className="card-title",
                            ),

                            # Form for Start and End Ports
                            dbc.Label("Start Port:", className='mt-2'),
                            dbc.Select(
                                id='start-port',
                                options=[{'label': port, 'value': port} for port in ['Mumbai', 'Chennai', 'Kolkata', 'Goa', 'Delhi', 'Dighi Port']],
                                value='Mumbai',
                                className='dropdown'
                            ),

                            dbc.Label("End Port:", className='mt-2'),
                            dbc.Select(
                                id='end-port',
                                options=[{'label': port, 'value': port} for port in ['Mumbai', 'Chennai', 'Kolkata', 'Goa', 'Delhi', 'Dighi Port']],
                                value='Chennai',
                                className='dropdown'
                            ),

                            dbc.Button(
                                'Recalculate Route',
                                id='button',
                                n_clicks=0,
                                className='custom-button mt-2',
                                style={
                                    "background-color": "black",
                                    "color": "white",
                                    "border": "none",
                                }
                            ),

                            # Route Distance Display
                            dbc.Alert(id='route-distance', color="info", className='mt-2'),

                        ]
                    ),
                    style=CARD_STYLE,  
                ),
                width=12,
            ),  # Add a closing comma here
        ),



        # Ship Path Section
        dbc.Row(
            dbc.Col(
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H4(
                                [DashIconify(icon="fa-solid:route", width=24), " Ship Path"], className="card-title"),
                            html.P("Below is the path the ship is currently taking, along with upcoming waypoints:",
                                   style={"font-size": "16px"}),
                            html.Iframe(
                                id='folium-map',
                                srcDoc=create_map('Mumbai', 'Chennai', get_port_coordinates)._repr_html_(),
                                width='100%',
                                height='400px',
                                style={'border': 'none'}
                            ),
                        ]
                    ),
                    style=CARD_STYLE,
                ),
                width=12
            ),
        ),
        
        # Footer Section
        dbc.Row(
            dbc.Col(
                html.Footer(
                    "© 2024 Matsya Navigation | Designed for optimal ship route tracking and navigation.",
                    className="text-center mt-4 p-4 bg-dark text-light",
                    style={"border-radius": "10px", "font-size": "14px"}
                ),
                width=12,
            )
        ),
    ]
)

# Callback to update map and route distance based on input
@app.callback(
    [Output('folium-map', 'srcDoc'),
     Output('route-distance', 'children')],
    [Input('button', 'n_clicks'),
     Input('start-port', 'value'),
     Input('end-port', 'value')]
)
def update_content(n_clicks, start_port, end_port):
    if n_clicks > 0:  # Only update if the button has been clicked
        # Update Folium map
        m = create_map(start_port, end_port, get_port_coordinates)
        map_html = m._repr_html_()

        # Calculate direct distance
        distance_info = calculate_sea_route(start_port, end_port)
        distance = distance_info.get('direct_distance_km', float('inf'))
        distance_text = f"Direct Distance: {distance:.2f} km" if distance != float('inf') else "Invalid ports specified"
        
        return map_html, distance_text
    return dash.no_update, dash.no_update  # Return no update if button hasn't been clicked

#Hamburger menu
@app.callback(
    Output("offcanvas-menu", "is_open"),
    Input("open-offcanvas", "n_clicks"),
    [dash.dependencies.State("offcanvas-menu", "is_open")],
)
def toggle_offcanvas(n_clicks, is_open):
    if n_clicks:
        return not is_open
    return is_open

if __name__ == '__main__':
    app.run_server(debug=True)
