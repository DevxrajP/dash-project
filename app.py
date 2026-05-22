from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

# Read CSV
df = pd.read_csv("formatted_output.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Create app
app = Dash(__name__)

# App Layout
app.layout = html.Div(
    style={
        "backgroundColor": "#f4f4f4",
        "padding": "20px",
        "fontFamily": "Arial"
    },
    children=[

        html.H1(
            "Soul Foods Sales Visualiser",
            style={
                "textAlign": "center",
                "color": "#d63384",
                "marginBottom": "30px"
            }
        ),

        html.Div([
            html.Label(
                "Filter by Region:",
                style={
                    "fontSize": "20px",
                    "fontWeight": "bold"
                }
            ),

            dcc.RadioItems(
                options=[
                    {"label": "All", "value": "all"},
                    {"label": "North", "value": "north"},
                    {"label": "East", "value": "east"},
                    {"label": "South", "value": "south"},
                    {"label": "West", "value": "west"},
                ],
                value="all",
                id="region-filter",
                inline=True,
                style={"marginTop": "10px"}
            )
        ]),

        dcc.Graph(id="sales-chart")
    ]
)

# Callback
@callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    sales_by_date = (
        filtered_df.groupby("date")["sales"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        sales_by_date,
        x="date",
        y="sales",
        title=f"Sales Data - {selected_region.title()} Region",
        labels={
            "date": "Date",
            "sales": "Sales"
        }
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="#f4f4f4",
        font=dict(size=14)
    )

    return fig

# Run app
if __name__ == "__main__":
    app.run(debug=True)