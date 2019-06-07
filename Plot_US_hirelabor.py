import numpy as np
import pandas as pd
import plotly
import plotly.graph_objs as go
import plotly.figure_factory as ff
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)

oper = pd.read_excel('Ag_Census_Map_data_07172015.xlsx', sheet_name='Operators')
# I want M123
# Average Age of Farm Workers
df = oper.iloc[:,[1,7]]
df.columns = ['fips','full_ownership']

counties = df['fips'].tolist()
full_ownership = df['full_ownership'].tolist()

heatmap_color = [
    'rgb(193, 193, 193)',
    'rgb(239, 239, 239)',
    'rgb(195, 196, 222)',
    'rgb(144,148,194)',
    'rgb(101,104,168)',
    'rgb(65, 53, 132)'
]

endpts = list(range(0, 100, 20))

fig = ff.create_choropleth(
	  fips = counties, values = full_ownership, colorscale = heatmap_color,
	  show_state_data = True,
	  binning_endpoints=endpts,
	  county_outline={'color': 'rgb(15,15,55)', 'width': 1},
	  state_outline={'color': 'rgb(15,15,55)', 'width': 1},
	  legend_title='Proportion (Percentage Point)',
	  title='Proportion of Full Ownership Farm arcoss Counties'
	  )
plotly.offline.plot(fig, filename = 'us_farm_ownership_prct.html')
