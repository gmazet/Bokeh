
from bokeh.plotting import figure, show, output_file
from bokeh.sampledata.iris import flowers
from sys import exit

import pandas as pd
import numpy as np

nb=100

def datetime(x):
        return np.array(x, dtype=np.datetime64)

#genre=[['femme','homme'][x] for x in np.random.random_integers(1,1,nb)]
#lateral=[['droite','gauche'][x] for x in np.random.random_integers(0,1,nb)]
age=np.random.random_integers(1,nb,nb)
dtindex=pd.date_range(start='2014-04-28 00:00', periods=nb, freq='H')
#df=pd.DataFrame({'Genre':genre, 'Lateral':lateral, 'Age':age, index:dtindex})
df2=pd.DataFrame(age, index=dtindex, columns=['Age'])
print df2
dt= datetime(df2.index)

#colormap = {'homme': 'red', 'femme': 'green', 'virginica': 'blue'}
#colors = [colormap[x] for x in df['Genre']]
#print colors

TOOLS="hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,"

p = figure(title = "test",x_axis_type="datetime", tools=TOOLS,plot_width=800, plot_height=400)
p.circle(df2.index,df2['Age'], fill_alpha=0.2, size=10)
output_file("iris.html", title="iris.py example")
show(p)
    
exit()
########################

colormap = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
print colormap
colors = [colormap[x] for x in flowers['species']]
print type(flowers)

p = figure(title = "Iris Morphology")
p.xaxis.axis_label = 'Petal Length'
p.yaxis.axis_label = 'Petal Width'

#p.circle(flowers["petal_length"], flowers["sepal_width"], color=colors, fill_alpha=0.2, size=10)
p.circle(s["petal_length"], flowers["sepal_width"], color=colors, fill_alpha=0.2, size=10)
output_file("iris.html", title="iris.py example")
show(p)
