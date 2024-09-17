import plotly.graph_objs as go

def plot_fuel_vs_route():
    # Sample data
    route_lengths = [100, 200, 300, 400, 500]
    fuel_consumption = [50, 70, 120, 160, 200]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=route_lengths, y=fuel_consumption, mode='lines+markers', name='Fuel Consumption'))
    fig.update_layout(title='Fuel Consumption vs Route Length', xaxis_title='Route Length (km)', yaxis_title='Fuel Consumption (liters)')
    
    return fig
