from obspy.clients.fdsn import Client as FDSN
from obspy.core.utcdatetime import UTCDateTime
from bokeh.plotting import figure, output_file, show
from bokeh.sampledata.stocks import AAPL
import pandas as pd

CL = FDSN("http://fdsnws.raspberryshakedata.com", timeout=5)

net='AM'
sta='R9F1B'
sta='RA3B7'
loc='00'
chan='SHZ'

t1 = UTCDateTime("2018-02-12T03:08:30.000")
t2=t1+1800

st = CL.get_waveforms(net, sta, loc, chan, t1, t2)
st=st[0]

print st.__doc__
print st.stats

#print st.stats.starttime# 2018-02-27T06:29:57.960000Z
#print st.stats.endtime# 2018-02-27T06:31:02.880000Z
rate=1.0/float(st.stats.sampling_rate)
npts=float(st.stats.npts)
print "%d samples" % npts

start=str(st.stats.starttime).replace('T',' ').replace('Z','')

df = pd.DataFrame(st.data,st.times(),columns=['data'])

output_file("rasp.html")

# create a new plot with a datetime axis type
p = figure(plot_width=1200, plot_height=450, x_axis_type="datetime")

p.line(df.index, df['data'], color='navy', alpha=0.5)

show(p)






