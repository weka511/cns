#!/usr/bin/env python

from alpha_neuron      import generate_spikes
from matplotlib.pyplot import plot, show
from numpy             import array, linspace



ts     = linspace(0.5,10,num=20)
counts = array([generate_spikes(t_peak)[2] for t_peak in ts])
plot(ts,counts)
plot([ts[0],ts[-1]],[counts[0],counts[-1]])
show()
