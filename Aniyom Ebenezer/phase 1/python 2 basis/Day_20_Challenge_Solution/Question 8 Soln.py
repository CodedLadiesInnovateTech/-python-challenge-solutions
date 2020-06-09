"""
Write a Python program to print the number of prime numbers which are less than or equal to a given integer.
"""
primes = [0]*50000
primes[0] = 0

for i in range(3,1000, 2):
    if primes[i // 2]:
        primes[(i * i)// 2::i]= [0] * len(primes[(i*i)//2::i])

n = int(input("Input The number(n): "))
if n < 4:
    print("Number of primes numbers which are less than or equal to n.: ", n-1)
else:
    print("Number of primes numbers which are less than or equal to n.: ", sum(primes[:(n+1)//2])+1)