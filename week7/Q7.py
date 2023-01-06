#!/usr/bin/env python

if __name__=='__main__':
    from pickle import load
    with open('c10p1.pickle','rb') as f:
        data = load(f)
        print (data.keys())

