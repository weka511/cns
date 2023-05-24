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

def alpha_n(V,a=0.01,b=10,c=10):
    return a*(V+b)/(np.exp((V+b)/c)-1)

def beta_n(V,a=0.125,b=80):
    return a*np.exp(V/b)

def alpha_m(V):
    return alpha_n(V,a=0.1,b=25)

def beta_m(V):
    return beta_n(V,a=4,b=10)

def alpha_h(V):
    return 0.07*np.exp(-V/20)

def beta_h(V):
    return 1/(np.exp((V+30)/10)+1)



if __name__=='__main__':
    parser = ArgumentParser(__doc__)
    parser.add_argument('--show', default=False, action='store_true', help='Controls whether plot will be displayed')
    parser.add_argument('--figs', default='./figs',                   help = 'Location for storing plot files')
    args = parser.parse_args()

    fig = figure(figsize=(12,12))
    ax1  = fig.add_subplot(2,1,1)
    V1 = np.linspace(-110,60,20)
    ax1.plot(V1,alpha_n(V1),label=r'$\alpha_n$')
    ax1.plot(V1,beta_n(V1),label=r'$\beta_n$')
    ax1.legend()
    ax2  = fig.add_subplot(2,1,2)
    V2 = np.linspace(-110,+10,20)
    ax2.plot(V2,alpha_m(V2),label=r'$\alpha_m$')
    ax2.plot(V2,beta_m(V2),label=r'$\beta_m$')
    ax2.plot(V2,alpha_h(V2),label=r'$\alpha_h$')
    ax2.plot(V2,beta_h(V2),label=r'$\beta_h$')
    ax2.legend()
    fig.savefig(join(args.figs,Path(__file__).stem))
    if args.show:
        show()

