#!/usr/bin/env python
'''
Created on Wed Apr 22 15:21:11 2015

Code to compute spike-triggered average.
'''

from __future__ import division
from numpy      import zeros

def compute_sta(stim, rho, num_timesteps):
    '''Compute the spike-triggered average from a stimulus and spike-train.

    Args:
        stim: stimulus time-series
        rho: spike-train time-series
        num_timesteps: how many timesteps to use in STA

    Returns:
        spike-triggered average for num_timesteps timesteps before spike'''

    sta = zeros((num_timesteps,))

    # This command finds the indices of all of the spikes that occur
    # after 300 ms into the recording.
    spike_times = rho[num_timesteps:].nonzero()[0] + num_timesteps
    num_spikes = len(spike_times)
    print (f'Number of spikes = {num_spikes}')

    # Compute the spike-triggered average of the spikes found.
    # To do this, compute the average of all of the vectors
    # starting 300 ms (exclusive) before a spike and ending at the time of
    # the event (inclusive). Each of these vectors defines a list of
    # samples that is contained within a window of 300 ms before each
    # spike. The average of these vectors should be completed in an
    # element-wise manner.

    for i in range(num_spikes):
        for j in range(num_timesteps):
            k = spike_times[i] - num_timesteps + j +1
            sta[j] += stim[k]
			
    return sta/num_spikes
