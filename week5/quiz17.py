#!/usr/bin/env python

from intfire import intfire
from matplotlib.pyplot import plot, show, title

tstop   = 200
Rates = []
for i in range(500):
    I = i/10
    n_spikes,V_trace = intfire(I=I,tstop=tstop)
    Rates.append(n_spikes/tstop)

plot(Rates)
title (f'{max(Rates)}/msec, or {int(1000*max(Rates))} Hertz')
show()
