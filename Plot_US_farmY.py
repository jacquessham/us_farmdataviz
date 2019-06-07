import numpy as np
import pandas as pd
import plotly
import plotly.figure_factory as ff
from plotly.offline import *


# To initiate ploty to run offline
init_notebook_mode(connected=True)

econ = pd.read_excel('Ag_Census_Map_data_07172015.xlsx', sheet_name='Economics')
# I want M048 (EBIT for crop sales)
# Also M258 (Payments from government)
df = econ.iloc[:,[1,94,142]]
df.columns = ['fips','Y_crop','Y_sub']

counties = df['fips'].tolist()
y_crop = df['Y_crop'].tolist()


heatmap_color = [
    'rgb(193, 193, 193)',
    'rgb(239, 239, 239)',
    'rgb(195, 196, 222)',
    'rgb(144,148,194)',
    'rgb(101,104,168)',
    'rgb(65, 53, 132)'
]

endpts = list(range(0,200000,40000))

fig = ff.create_choropleth(
	  fips = counties, values = y_crop, colorscale = heatmap_color,
	  show_state_data = True,
	  binning_endpoints=endpts,
	  county_outline={'color': 'rgb(15,15,55)', 'width': 1},
	  state_outline={'color': 'rgb(15,15,55)', 'width': 1},
	  legend_title='USD',
	  title='Income from Crops per Farm on Average arcoss Counties'
	  )
plotly.offline.plot(fig, filename = 'us_farm_income.html')
