class Solution:
    def climbStairs(self, n: int) -> int:
        a = 0
        b = 1
        for i in range(n-1):
            a = b
            b = a+b
        return a 


def fib(n):
    a = 0
    b = 1
    if n <= 2:
        return n
    
    a = 0
    b = 1
    for i in range(n):
        temp = a
        a = b
        b = temp+b
    return a

for i in range(10):
    print(fib(i))