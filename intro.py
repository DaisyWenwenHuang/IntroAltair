import pandas as pd
import altair as alt
# world happiness data 2016
data = pd.read_csv("WHR_2016.csv")
data.head()

alt.Chart(data).mark_bar().encode(
	x = 'Region',
	y = 'Happiness Score'
)



