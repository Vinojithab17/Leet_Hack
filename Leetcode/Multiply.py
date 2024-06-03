print(ord('1'))
print(ord('2'))

num1 = "123"
num2 = "456"
l1 = len(num1)
l2 = len(num2)
a = 0
b = 0

for i in range(l1):
    a += (ord(num1[i])-48)*10**(l1 - i -1)
for i in range(l2):
    b += (ord(num2[i])-48)*10**(l2 - i -1)

print(str(a*b))


a = [0]
a = a*2
print(a)