from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# Read processed CSV file
df = pd.read_csv("formatted_output.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by date
df = df.sort_values("date")

# Group sales by date
sales_by_date = df.groupby("date")["sales"].sum().reset_index()

# Create line chart
fig = px.line(
    sales_by_date,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time",
    labels={
        "date": "Date",
        "sales": "Sales"
    }
)

# Create Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1(
        "Soul Foods Sales Visualiser",
        style={"textAlign": "center"}
    ),

    dcc.Graph(
        figure=fig
    )
])

if __name__ == "__main__":
    app.run(debug=True)