from obspy.clients.fdsn import Client as FDSN
from obspy.core.utcdatetime import UTCDateTime
from datetime import timedelta
from bokeh.plotting import figure, output_file, show
from bokeh.sampledata.stocks import AAPL
from bokeh.models import DatetimeTickFormatter
import pandas as pd
import numpy as np
import time
from calendar import timegm

CL = FDSN("http://fdsnws.raspberryshakedata.com", timeout=5)

net='AM'
sta='RA3B7'
sta='R9F1B'
loc='00'
chan='SHZ'

t1 = UTCDateTime("2018-02-12T03:08:30.000")
t2=t1+300

st = CL.get_waveforms(net, sta, loc, chan, t1, t2)
st=st[0]

#print st.__doc__
#print st.stats

starttime=st.stats.starttime# 2018-02-27T06:29:57.960000Z
endtime=st.stats.endtime# 2018-02-27T06:31:02.880000Z

start_utc_time = time.strptime(str(starttime), "%Y-%m-%dT%H:%M:%S.%fZ")
start_epoch_time = timegm(start_utc_time)

mydatetime=[]
mytunix=[]
for tt in st.times():
    tunix=start_epoch_time + tt
    mytunix.append(tunix)
    mydatetime.append(pd.to_datetime(tunix, unit='s'))
mydatetime=np.asarray(mydatetime)
mytunix=np.asarray(mytunix)

print type(st.times()[0]), type(mydatetime[0])

npts=float(st.stats.npts)
print "%d samples" % npts

df = pd.DataFrame(st.data,mydatetime,columns=['counts'])
df['tunix']=mytunix
print df

output_file("rasp.html")

p = figure(plot_width=1200, plot_height=450, x_axis_type="datetime")
#p.line(df.index, df['counts'], color='navy', alpha=0.5)
p.line(mydatetime, df['counts'], color='navy', alpha=0.5)

p.xaxis.formatter=DatetimeTickFormatter(
        milliseconds=["%H:%M:%S.%3N"],
        seconds=["%d/%m/%Y %T"],
        minsec=["%d/%m/%Y %T"],
        minutes=["%d/%m/%Y %T"],
        hourmin=["%d/%m/%Y %T"],
        hours=["%d/%m/%Y %T"],
        days=["%d/%m/%Y"],
        months=["%d/%m/%Y"],
        years=["%d/%m/%Y"],
)
p.xaxis.major_label_orientation = np.pi/4

show(p)

