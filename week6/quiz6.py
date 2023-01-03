#!/usr/bin/env python

from alpha_neuron      import generate_spikes
from matplotlib.pyplot import plot, show
from numpy             import arange, array

def count(t_peak):
    t_trace,V_trace,spike_counter=generate_spikes(t_peak)
    return spike_counter

ts = arange(0.5,10.5,0.5)
counts = array([count(t_peak) for t_peak in ts])
plot(ts,counts)
plot(ts,ts)
show()
