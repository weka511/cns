#!/usr/bin/env python
"""
Created on Wed Apr 22 15:15:16 2015

Quiz 2 code.
"""

from __future__        import division
from numpy             import arange
from matplotlib.pyplot import figure, show
from pickle            import load
from compute_sta       import compute_sta



def get_data(file_name = 'c1p8.pickle'):
    with open(file_name, 'rb') as f:
        data = load(f)
        return data['stim'], data['rho']

stim, rho       = get_data()
sampling_period = 2 # in ms
num_timesteps   = 148
sta             = compute_sta(stim, rho, num_timesteps)
time            = (arange(-num_timesteps, 0) + 1) * sampling_period

N_window        = 160
fig             = figure(figsize=(16,10))
ax1             = fig.add_subplot(2,1,1)
ax1a            = ax1.twinx()
ax2             = fig.add_subplot(2,1,2)

ax1.plot (stim[0:N_window],c='xkcd:blue')
ax1a.plot (rho[0:N_window],'ro')
ax1.set_ylabel('stim',c='xkcd:blue')
ax1a.set_ylabel('rho',c='xkcd:red')
ax2.plot(time, sta)
ax2.set_xlabel('Time (ms)')
ax2.set_ylabel('Stimulus')
ax2.set_title('Spike-Triggered Average')
show()
