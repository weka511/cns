#!/usr/bin/env python

from argparse          import ArgumentParser
from matplotlib.pyplot import figure,  show
from numpy             import argmax, array, corrcoef, matmul, mean
from numpy.linalg      import eig
from numpy.random      import default_rng
from os.path           import exists
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
        for i in range(M):
            self.update(X[i,:])

if __name__=='__main__':
    parser = ArgumentParser()
    parser.add_argument('--offset', nargs=2, default = [0,0], type=float)
    parser.add_argument('--alpha', default=1, type=float)
    args   = parser.parse_args()
    offset = array(args.offset)
    with open('c10p1.pickle','rb') as f:
        data      = load(f)['c10p1']
        M,N       = data.shape
        data_mean = mean(data,axis=0)
        X         = data - data_mean + offset
        Q         = corrcoef(X.transpose())
        w,v       = eig(Q)

        oja       = Oja(N=N,alpha=args.alpha)
        for i in range(2501):
            oja.learn(X)
            if i%500==0:
                print (f'Iteration {i}')
        print (f'Weights {oja.W}')
        print(w)
        print(v)
        k = argmax(w)
        print (w[k])
        print (v[:,k])
        fig = figure(figsize=(12,6))
        ax1 = fig.add_subplot(1,2,1)
        ax1.scatter(data[:,0],data[:,1])
        ax1.set_title(f'{offset}')
        ax2 = fig.add_subplot(1,2,2)
        ax2.axis([0, 10, 0, 10])
        ax2.text(1,9,f'Eigenvalues {w}')
        ax2.text(1,8,f'Eigenvectors {v}')
        ax2.text(1,7,f'Weights {oja.W}')
        for i in range(1,11):
            path_name = f'{args.offset[0]}-{args.offset[1]}-{i}'.replace('.','-')
            if not exists(f'{path_name}.png'):
                fig.savefig(path_name)
                break
    show()
