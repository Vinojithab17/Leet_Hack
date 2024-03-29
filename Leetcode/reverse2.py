a = 1234
b = 0 

print(b)

while a > 0:
    b = a%10 + b*10
    a = a//10

print(b)