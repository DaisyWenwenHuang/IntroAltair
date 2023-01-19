import pandas as pd
import altair as alt
# world happiness data 2016
data = pd.read_csv("WHR_2016.csv")
data.head()

# bar plot
alt.Chart(data).mark_bar().encode(
	x = 'Region',
	y = 'Happiness Score'
)

# scatter plot 1
healthPlot = alt.Chart(data).mark_circle().encode(
	x = 'Health(Life Expectancy)',
	y = 'Happiness Score',
	color = alt.Color('Region',scale = alt.Scale(scheme='spectral')),
	tooltip = ['Country','Happiness Score'],
)

# scatter plot 2
generosityPlot = alt.Chart(data).mark_circle().encode(
	x = 'Generosity',
	y = 'Happiness Score',
	color = alt.Color('Region',scale = alt.Scale(scheme='spectral')),
	tooltip = ['Country','Happiness Score'],
)

# focet scatter plot 1 and 2
healthPlot | generosityPlot

# line graph
linegraph = alt.Chart(data).mark_line().encode(
	x = 'Happiness Rank',
	y = 'Health(Life Expectancy)'
)

linegraph.save('linegraph.html',embed_options={'render':'svg'})