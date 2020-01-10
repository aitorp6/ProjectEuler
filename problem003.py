"""
https://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?


@author: https://github.com/aitorp6
"""
from math import sqrt

def isPrime(n):
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True
    
    
num = 600851475143
i = 2
largest = 2
while i <= int(sqrt(num)) + 1:
    i += 1
    if num % i == 0:
        if isPrime(i) == True and i > largest:
            largest = i 
            
print("The largest prime factor of the number 600851475143 is {}.".format(largest))
        

