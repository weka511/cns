#!/usr/bin/env python

from matplotlib.pyplot import figure,  show
from numpy             import corrcoef, matmul, mean
from numpy.linalg      import eig
from numpy.random      import default_rng
from pickle            import load

class Oja:
    def __init__(self,
                 DeltaT = 0.01,
                 eta    = 1,
                 alpha  = 1,
                 N      = 2,
                 rng    = default_rng()):
        self.rng    = rng
        self.DeltaT = DeltaT
        self.eta    = eta
        self.alpha  = alpha
        self.W      = self.rng.random((N,N)) - 0.5


    def update(self,u):
        v       = matmul(u,self.W)
        self.W += self.DeltaT * self.eta * (matmul(v,u) - self.alpha * ( v * v) * self.W)

    def learn(self,X):
        M,_  = X.shape
        for i in range(M):#self.rng.choice(M,size=M,replace=False):
            self.update(X[i,:])

if __name__=='__main__':
    with open('c10p1.pickle','rb') as f:
        data      = load(f)['c10p1']
        M,N       = data.shape
        data_mean = mean(data,axis=0)
        X         = data - data_mean
        Q         = corrcoef(X.transpose())
        w,v       = eig(Q)
        oja       = Oja(N=N)
        for i in range(10000):
            oja.learn(X)
            if i%1000==0:
                print (f'Iteration {i}')
                print (oja.W)
        fig = figure(figsize=(5,10))
        ax1 = fig.add_subplot(2,1,1)
        ax1.scatter(data[:,0],data[:,1])

        ax2 = fig.add_subplot(2,1,2)
        ax2.scatter(X[:,0],X[:,1])

    show()
