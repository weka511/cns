#!/usr/bin/env python

# from __future__ import print_function
'''
Created on Wed Apr 22 16:02:53 2015

Basic integrate-and-fire neuron
R Rao 2007

translated to Python by rkp 2015
'''

from matplotlib.pyplot import plot, show, title

def intfire(I       = 1 ,
            C       = 1,
            R       = 40,
            tstop   = 200,
            abs_ref = 5,
            V_th    = 10):
   '''
   I & F implementation dV/dt = - V/RC + I/C
   Using h = 1 ms step size, Euler method

   Parameters:
       I       input current nA
       C       capacitance  nF
       R       leak resistance M ohms
       tstop   trial duration
       abs_ref absolute refractory period
       V_th    spike threshold
   '''
   V        = 0
   ref      = 0 # absolute refractory period counter
   V_trace  = []  # voltage trace for plotting

   n_spikes = 0
   for t in range(tstop):
      if not ref:
            V = V - (V/(R*C)) + (I/C)
      else:
            ref -= 1
            V    = 0.2 * V_th # reset voltage

      if V > V_th:
         V         = 50 # emit spike
         ref       = abs_ref # set refractory counter
         n_spikes += 1
      V_trace += [V]
   return n_spikes,V_trace

if __name__=='__main__':
   n_spikes,V_trace = intfire()
   plot(V_trace)
   title(f'{n_spikes} spikes')
   show()
