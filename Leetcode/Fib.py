a = 0
b = 1


for i in range(10):
    a,b = b,a+b
    # print(a)
        
        
print(a)


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(10): 
    print(fibonacci(i))
