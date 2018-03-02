import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.sampledata.stocks import AAPL
import sys

print type(AAPL)
print AAPL.keys()
sys.exit()
df = pd.DataFrame(AAPL)
df2 = pd.DataFrame(AAPL)

df['date'] = pd.to_datetime(df['date'])
print len(df)
df2['date'] = pd.to_datetime(df2['date'])

df2["date"] = df2["date"].apply(pd.DateOffset(years=13))
df=df.append(df2)
print len(df)
df2=df.copy()
df2["date"] = df2["date"].apply(pd.DateOffset(years=26))
df=df.append(df2)
print len(df)
df2=df.copy()
df2["date"] = df2["date"].apply(pd.DateOffset(years=52))
df=df.append(df2)
print len(df)
df2=df.copy()
df2["date"] = df2["date"].apply(pd.DateOffset(years=104))
df=df.append(df2)
print len(df)
df2=df.copy()
df2["date"] = df2["date"].apply(pd.DateOffset(years=208))
df=df.append(df2)
print len(df)


output_file("datetime.html")

# create a new plot with a datetime axis type
p = figure(plot_width=1200, plot_height=450, x_axis_type="datetime")

p.line(df['date'], df['close'], color='navy', alpha=0.5)

show(p)

