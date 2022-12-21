#!/usr/bin/env python

from matplotlib.pyplot import figure, show
from numpy             import argmin, array, exp, linspace, pi, sqrt, zeros
from scipy.integrate   import simpson
from scipy.optimize    import minimize
from scipy.stats       import norm

class Distribution:
    def __init__(self,loc=0,scale=1):
        self.loc   = loc
        self.scale = scale

    def get_pdf(self,xs):
        return norm.pdf(xs, self.loc,self.scale)

    def get_cdf(self,xs):
        return norm.cdf(xs, self.loc,self.scale)

    def get_area(self,i,xs,
                 direction = +1):
        ys = self.get_pdf(xs)
        if direction==+1:
            return simpson(ys[i:],xs[i:])
        if direction==-1:
            return simpson(ys[:i+1],xs[:i+1])

def get_loss(z, d1, d2,
             priors = [0.5, 0.5],
             costs  = [1.0, 2.0]):
    p_call_1_given_2 = 1 - d1.get_cdf(z)
    p_call_2_given_1 = d2.get_cdf(z)
    p_wrong_call_1   = p_call_1_given_2 * priors[1]
    p_wrong_call_2   = p_call_2_given_1 *priors[0]
    return costs[1]*p_wrong_call_2 + costs[0]*p_wrong_call_1

if __name__=='__main__':
    xs     = linspace(0,12,2000)
    d1     = Distribution(loc=5,scale=0.5)
    d2     = Distribution(loc=7,scale=1.0)
    y1s    = d1.get_pdf(xs)
    y2s    = d2.get_pdf(xs)
    losses = get_loss(xs,d1,d2)
    i      = argmin(losses)
    xmin   = minimize(lambda x:get_loss(x,d1,d2), xs[i]).x[0]

    fig    = figure(figsize=(12,12))
    ax1    = fig.add_subplot(1,1,1)
    ax1.plot(xs,y1s,
             label = rf'$\mu={5}$, $\sigma={0.5}$',
             c     = 'xkcd:green')
    ax1.plot(xs,y2s,
             label = rf'$\mu={7}$, $\sigma={1.0}$',
             c     = 'xkcd:purple')
    ax1.plot(xs,losses,label='Losses',c='xkcd:red')
    ax1.vlines(xmin,0,1,linestyles='dashed', label=f'xmin={xmin:.4f}',color='xkcd:blue')
    ax1.fill_between(xs[i:],y1s[i:],
                     hatch     = '/',
                     label     = rf'$p[2\vert 1]$, Area={d1.get_area(i,xs,direction=-1):.4f}',
                     color     = 'xkcd:lime',
                     edgecolor = 'xkcd:black')
    ax1.fill_between(xs[:i+1],y2s[:i+1],
                     hatch     = '\\',
                     label     = rf'$p[1\vert 2]$, Area={d2.get_area(i,xs,direction=+1):.4f}',
                     color     = 'xkcd:cyan',
                     edgecolor = 'xkcd:black')
    ax1.legend()
    fig.savefig('quiz1')
    show()
