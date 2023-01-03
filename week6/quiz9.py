#!/usr/bin/env python


from numpy        import array, matmul, zeros_like
from numpy.linalg import eig

W = array([[0.6, 0.1, 0.1, 0.1, 0.1],
           [0.1, 0.6, 0.1, 0.1, 0.1],
           [0.1, 0.1, 0.6, 0.1, 0.1],
           [0.1, 0.1, 0.1, 0.6, 0.1],
           [0.1, 0.1, 0.1, 0.1, 0.6 ]])

u =array([0.6, 0.5, 0.6, 0.2, 0.1])




M = 0.75 * array([[-1,  0, 1,  1, 0],
                  [ 0, -1, 0,  1, 1],
                  [ 1, 0, -1,  0, 1],
                  [ 1, 1,  0, -1, 0],
                  [ 0, 1,  1, 0, -1]] )

h = matmul(W,u)

lambdaM,e = eig(M)

v_ss = zeros_like(u)
for i in range(len(lambdaM)):
    v_ss += (matmul(h,e[:,i])/(1-lambdaM[i]))*e[:,i]
print (v_ss)
