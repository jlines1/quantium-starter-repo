#import required libraries
import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

#init
app = Dash()

#import data
df = pd.read_csv("data/cleaned_sales.csv")

#create line graph
fig = px.line(df, x="date", y='sales', title='Revenue over time')

app.layout = html.Div(children = [
    #Create Header
    html.H1("Revenue over time"),

    #display line graph
    dcc.Graph(
        id="Revenue Linegraph",
        figure=fig
    )

])

#Add header

#Add line chart
#read in data

if __name__ == '__main__':
    app.run(debug=True)