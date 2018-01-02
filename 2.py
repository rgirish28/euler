#!/usr/bin/python

from math import sqrt
def F(n):
        return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

sum = 0
i =1

while(int(F(i))<4000000):
    if int(F(i))%2 is 0:
        sum+=int(F(i))
    i=i+1
print sum
