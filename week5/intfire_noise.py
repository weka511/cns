#!/usr/bin/env python

from __future__ import print_function
"""
Created on Wed Apr 22 16:02:53 2015

Basic integrate-and-fire neuron
R Rao 2007

translated to Python by rkp 2015
"""

import numpy as np
from matplotlib.pyplot import figure, hist, legend, plot, show

def intfire(I        = 1,
            C        = 1,
            R        = 40,
            tstop    = 200,
            abs_ref  = 5,
            V_th     = 10,
            noiseamp = 1):
   '''

   Parameters:
       I        input current   nA
       C        capacitance     nF
       R        leak resistance M ohms
       tstop    Stopping time
       abs_ref  absolute refractory period
       V_th     spike threshold
       noiseamp amplitude of added noise
   '''

   # I & F implementation dV/dt = - V/RC + I/C
   # Using h = 1 ms step size, Euler method

   V       = 0
   ref     = 0 # absolute refractory period counter
   V_trace = []  # voltage trace for plotting

   spiketimes = [] # list of spike times

   I += noiseamp*np.random.normal(0, 1, (tstop,)) # nA; Gaussian noise

   for t in range(tstop):

      if not ref:
         V = V - (V/(R*C)) + (I[t]/C)
      else:
         ref -= 1
         V = 0.2 * V_th # reset voltage

      if V > V_th:
         V = 50 # emit spike
         ref = abs_ref # set refractory counter
         spiketimes.append(t)
      V_trace += [V]
   return V_trace,spiketimes

if __name__=='__main__':
   fig = figure()
   for noiseamp in range(5*2):
      ax = fig.add_subplot(5,2,noiseamp+1)
      V_trace,spiketimes = intfire(noiseamp=(noiseamp+1)/2,tstop=2000)
      # plot(V_trace)
      spike_intervals = [b-a for a,b in zip(spiketimes[:-1],spiketimes[1:])]
      ax.hist(spike_intervals)#,label=f'{I}')
   # legend()
   show()
