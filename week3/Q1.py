from matplotlib.pyplot import figure, show
from numpy             import exp, linspace, pi, sqrt, zeros
from scipy.optimize    import fsolve
from scipy.stats       import norm



xs = linspace(0,12,100)
y1s = norm.pdf(xs,loc=5,scale=0.5)
y2s = norm.pdf(xs,loc=7,scale=1.0)
x0  = fsolve(lambda x:norm.pdf(x,loc=5,scale=0.5) -  norm.pdf(x,loc=7,scale=1.0), 6)
fig = figure(figsize=(6,6))
ax1 = fig.add_subplot(1,2,1)
ax1.plot(xs,y1s,label=rf'$\mu={5}$, $\sigma={0.5}$')
ax1.plot(xs,y2s,label=rf'$\mu={7}$, $\sigma={1.0}$')
ax1.vlines(x0,0,1,linestyles='dotted', label=f'{x0[0]}')
ax1.legend()
show()
