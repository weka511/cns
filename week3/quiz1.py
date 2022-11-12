#!/usr/bin/env python

from matplotlib.pyplot import figure, show
from numpy             import argmin, array, exp, linspace, pi, sqrt, zeros
from scipy.integrate   import simpson
from scipy.optimize    import minimize
from scipy.stats       import norm

def get_loss(z,
             costs  = array([1.0, 2.0]),
             priors = array([0.5, 0.5]),
             locs   = array([5.0, 7.0]),
             scales = array([0.5, 1.0])):
    p_call_1_given_2 = 1 - norm.cdf(z,loc=locs[0],scale=scales[0])
    p_wrong_call_1   = p_call_1_given_2 * priors[1]
    p_call_2_given_1 = norm.cdf(z,loc=locs[1],scale=scales[1])
    p_wrong_call_2   = p_call_2_given_1 *priors[0]
    return costs[1]*p_wrong_call_2 + costs[0]*p_wrong_call_1

if __name__=='__main__':
    xs     = linspace(0,12,2000)
    y1s    = norm.pdf(xs,loc=5,scale=0.5)
    y2s    = norm.pdf(xs,loc=7,scale=1.0)
    losses = get_loss(xs)
    i      = argmin(losses)
    xmin   = minimize(get_loss,xs[i])
    a1     = simpson(y1s[i:],xs[i:])
    a2     = simpson(y2s[:i+1],xs[:i+1])
    fig    = figure(figsize=(12,12))
    ax1    = fig.add_subplot(1,1,1)
    ax1.plot(xs,y1s,label=rf'$\mu={5}$, $\sigma={0.5}$',c='xkcd:green')
    ax1.plot(xs,y2s,label=rf'$\mu={7}$, $\sigma={1.0}$',c='xkcd:purple')
    ax1.plot(xs,losses,label='Losses',c='xkcd:red')
    ax1.vlines(xmin.x[0],0,1,linestyles='dashed', label=f'xmin={xmin.x[0]:.4f}',color='xkcd:blue')
    ax1.fill_between(xs[i:],y1s[i:],
                     hatch     = '/',
                     label     = rf'$p[2\vert 1]$, Area={a1:.4f}',
                     color     = 'xkcd:lime',
                     edgecolor = 'xkcd:black')
    ax1.fill_between(xs[:i+1],y2s[:i+1],
                     hatch     = '\\',
                     label     = rf'$p[1\vert 2]$, Area={a2:.4f}',
                     color     = 'xkcd:cyan',
                     edgecolor = 'xkcd:black')
    ax1.legend()
    show()
