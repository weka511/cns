#!/usr/bin/env python

from matplotlib.pyplot import figure, show
from numpy             import argmin, array, exp, linspace, pi, sqrt, zeros
from scipy.optimize    import fsolve, minimize
from scipy.stats       import norm

def get_loss(z,
             costs = array([1,2]),
             priors = array([0.5,0.5])):
    p_wrong_call_1_given_2 = 1 - norm.cdf(z,loc=5,scale=0.5)
    p_wrong_call_1         = p_wrong_call_1_given_2 * priors[1]
    p_wrong_call_2_given_1 = norm.cdf(z,loc=7,scale=1.0)
    p_wrong_call_2         = p_wrong_call_2_given_1 *priors[0]
    return costs[1]*p_wrong_call_2 + costs[0]*p_wrong_call_1

if __name__=='__main__':
    xs     = linspace(0,12,100)
    y1s    = norm.pdf(xs,loc=5,scale=0.5)
    y2s    = norm.pdf(xs,loc=7,scale=1.0)
    # x0     = fsolve(lambda x:norm.pdf(x,loc=5,scale=0.5) -  norm.pdf(x,loc=7,scale=1.0), 6)
    losses = get_loss(xs)
    i      = argmin(losses)
    xmin   = minimize(get_loss,xs[i])
    fig    = figure(figsize=(12,12))
    ax1   = fig.add_subplot(1,1,1)
    ax1.plot(xs,y1s,label=rf'$\mu={5}$, $\sigma={0.5}$',c='xkcd:green')
    ax1.plot(xs,y2s,label=rf'$\mu={7}$, $\sigma={1.0}$',c='xkcd:purple')
    # ax1.vlines(x0,0,1,linestyles='dotted', label=f'{x0[0]}')
    ax1.plot(xs,losses,label='Losses',c='xkcd:red')
    ax1.vlines(xmin.x[0],0,1,linestyles='dashed', label=f'xmin={xmin.x[0]:.4f}',color='xkcd:blue')
    ax1.legend()
    show()
