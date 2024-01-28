import math


n = 2



def isPrime(n):
    if(n <= 1):
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
print(isPrime(15))
print(isPrime(13))
print(isPrime(75))
print(isPrime(121))
    