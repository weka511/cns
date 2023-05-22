#!/usr/bin/env python

# Copyright (C) 2023 Simon Crase  simon@greenweaves.nz

# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GNU Emacs.  If not, see <http://www.gnu.org/licenses/>.

'''Hodgkin-Huxley Model'''


# Standard library imports.

from argparse import ArgumentParser
from os.path  import join
from pathlib  import Path

# Related third party imports.

from matplotlib.pyplot import figure, show
import numpy as np

# Local application/library specific imports.

def euler(func, y0, t):
    y  = np.zeros((np.size(t)))
    y[0] = y0

    for i in range(0,np.size(t) - 1):
        dt  = t[i + 1] - t[i]
        y[i + 1] = y[i] + dt*func(y[i], t[i])

    return y

def alpha(V,a=0.01,b=10,c=10):
    return 0.01*(b-V)/(np.exp((b-V)/c)-1)

def beta(V,a=0.125,b=80):
    return a*np.exp(-V/b)

def func(y,t,V=-50,alpha = alpha,beta = beta):
    return alpha(V)*(1-y) - beta(V)*y



def alpha_h(V):
    return 0.07*np.exp(-V/20)

def beta_h(V):
    return 1/(np.exp((30-V)/10)+1)

if __name__=='__main__':
    parser = ArgumentParser(__doc__)
    parser.add_argument('--show', default=False, action='store_true', help='Controls whether plot will be displayed')
    parser.add_argument('--figs', default='./figs',                   help = 'Location for storing plot files')
    args = parser.parse_args()

    tInitial = 0
    tFinal = 10
    Nt = 5000
    tArray = np.linspace(tInitial, tFinal, Nt)
    n0 = 1.0
    ns = euler(func, n0, tArray)
    m0 = 1.0
    ms = euler(lambda y,t: func(y,t,alpha=lambda V:alpha(V,a=0.1,b=25),beta=lambda V:beta(V,a=4,b=18)),m0,tArray)
    h0 = 1.0
    hs = euler(lambda y,t: func(y,t,alpha=alpha_h,beta=beta_h),h0,tArray)
    fig = figure()
    ax  = fig.add_subplot(1,1,1)
    ax.plot(ns,label='n')
    ax.plot(ms,label='m')
    ax.plot(hs,label='h')
    ax.legend()
    fig.savefig(join(args.figs,Path(__file__).stem))
    if args.show:
        show()

