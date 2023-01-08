#!/usr/bin/env python

from numpy        import argmax, array, matmul
from numpy.linalg import eig

Q = array([[0.2, 0.1],
           [0.1, 0.3]])

w,v = eig(Q)
for i in range(2):
    print (f'lambda = {w[i]}')
    print (f'v={v[:,i]}')
i   = argmax(w)
print (f'principal eigenvalue={v[:,i]}')

ww1 = array([0.8944,  1.7889])
ww2 = array([-1.5155, -1.3051])
ww3 = array([-1.5764, -1.2308])
ww4 = array([1.0515,  1.7013])
for ww in [ww1,ww2,ww3,ww4]:
    print(ww,v[:,i]/ww)
