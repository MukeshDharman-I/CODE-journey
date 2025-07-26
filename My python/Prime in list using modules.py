from sympy import isprime
prime=[]
for i in range(2,1200):
    if isprime(i):
        prime.append(i)
    else:
        del i
print(prime)        