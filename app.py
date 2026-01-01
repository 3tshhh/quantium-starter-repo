# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
app = Dash()

df = pd.read_csv("./filtered_data.csv")
df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

df = (
    df.groupby("Date", as_index=False)["Sales"]
    .sum()
    .sort_values("Date")
)

fig = px.line(
    df,
    x="Date",
    y="Sales",
    labels={
        "date": "Date",
        "Sales": "Total Sales"
    }
)


app.layout = html.Div(
    children=[
        html.H1("Pink Morsel Sales Over Time"),
        dcc.Graph(
            id="Sales-over-time",
            figure=fig
        )
    ]
)

if __name__ == "__main__":
    app.run(debug=True)

