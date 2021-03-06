import csv 
import plotly.express as px

with open("Cups of coffee & Hours of sleep.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df, x="Coffee in ml",y= "sleep in hours",color = "week")
    fig.show()