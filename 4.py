#!/usr/bin/python


def palindrome(s):
    if s[::-1] == s:
        return True
    else:
        return False

largest = 0

for i in range(100,1000):
    for j in range(i,1000):
        prod = i*j
        if palindrome(str(prod)) and prod > largest:
            largest = prod


print palindrome(str(1001))

print largest
