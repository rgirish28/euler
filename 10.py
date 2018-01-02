#!/usr/bin/python

from math import sqrt

n = 2000000
seive = [True for i in range(1,n+1)]


def gen_seive(n,seive):
    for i in range(2,int(sqrt(n)+1)):
        for j in range(2,int(n/i)+1):
            if i*j < n:
                seive[i*j] = False

seive[1] = False

gen_seive(n,seive)


def prime(seive):
    sum = 0
    for i in range(1,len(seive)):
        if seive[i] is True:
            sum=sum+i
    
    print sum


prime(seive)



