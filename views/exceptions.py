import plotly.express as px
import pandas as pd

df = pd.read_json("exceptions.json")
fig = px.line(df, x="DATE", y="DISTINCT_USERS", title='Daily user exceptions')

fig.write_html("index.html")