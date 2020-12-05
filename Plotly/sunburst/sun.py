import plotly.express as px
import pandas as pd
import numpy as np

data = pd.read_csv('MPVDataset.csv')
data = data[data['State'].isin(["NY", "CA", "TX"])]
data = data[data["Victim\'s race"].isin(
    ["White", "Black", "Hispanic", "Asian"])]

fig = px.sunburst(data, path=["Unarmed", "State", "Victim's race"],
                  color="Unarmed", color_discrete_sequence=px.colors.qualitative.Pastel,maxdepth=-1)
fig.show()
