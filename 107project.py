import csv
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("107projectdata.csv")
print(df.groupby("level")["attempt"].mean())

fig = go.Figure(go.Scatter(
    x = df.groupby("level")["attempt"].mean(),
    y = ["level 1","level 2","level 3","level 4"]
))

fig.show()