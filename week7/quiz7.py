#!/usr/bin/env python

from matplotlib.pyplot import scatter,show
from pickle            import load

def display(points):
    scatter(points[:,0],points[:,1])

if __name__=='__main__':

    with open('c10p1.pickle','rb') as f:
        data = load(f)
        display(data['c10p1'])

    show()
