import pandas as pd
import plotly.express as px

def generate_service_chart(data_type, user_data=None):
    if data_type == "Popular Services":
        if user_data:
            df = pd.DataFrame(user_data)
        else:
            df = pd.DataFrame({
                "Service": ["Oil Change", "Tire Rotation", "Brake Service", "Engine Tune-up", "A/C Service"],
                "Percentage": [30, 25, 20, 15, 10]
            })
        fig = px.pie(df, values="Percentage", names="Service", title="Popular Garage Services")
    elif data_type == "Average Service Costs":
        if user_data:
            df = pd.DataFrame(user_data)
        else:
            df = pd.DataFrame({
                "Service": ["Oil Change", "Tire Rotation", "Brake Service", "Engine Tune-up", "A/C Service"],
                "Cost": [50, 30, 200, 150, 100]
            })
        fig = px.bar(df, x="Service", y="Cost", title="Average Service Costs")
    return fig