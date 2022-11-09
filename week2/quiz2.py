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

FILENAME = 'c1p8.pickle'

with open(FILENAME, 'rb') as f:
    data = load(f)
    stim            = data['stim']
    rho             = data['rho']
    N               = 100
    sampling_period = 2 # in ms
    num_timesteps   = 148
    sta             = compute_sta(stim, rho, num_timesteps)
    time            = (arange(-num_timesteps, 0) + 1) * sampling_period

    fig             = figure(figsize=(10,10))
    ax1             = fig.add_subplot(2,1,1)
    ax1a            = ax1.twinx()
    ax2             = fig.add_subplot(2,1,2)
    ax1.plot (stim[0:N],c='xkcd:blue')
    ax1a.plot (rho[0:N],'ro')
    ax1.set_ylabel('stim',c='xkcd:blue')
    ax1a.set_ylabel('rho',c='xkcd:red')
    ax2.plot(time, sta)
    ax2.set_xlabel('Time (ms)')
    ax2.set_ylabel('Stimulus')
    ax2.set_title('Spike-Triggered Average')
    show()
