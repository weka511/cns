#!/usr/bin/env python

'''Answer to Q 16 (largest current that will fail to cause neuron to spike)'''

from intfire           import intfire
from matplotlib.pyplot import legend, plot, show, title

I0 = 0
I1 = 1

while I1-I0>0.0005:
    I                = 0.5*(I0+I1)
    n_spikes,V_trace = intfire(I=I)
    if n_spikes==0:
        I0 = I
    else:
        I1 = I
    print (I0,I1,I,n_spikes)

n_spikes0,V_trace0 = intfire(I=I0)
plot (V_trace0,label=f'{I0}')
n_spikes,V_trace1 = intfire(I=I1)
plot (V_trace1,label=f'{I1}')
legend()

title (f'{int(1000*I0)}')
show()
