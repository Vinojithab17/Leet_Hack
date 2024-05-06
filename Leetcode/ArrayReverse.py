a = [1,2,3,4,5,6,7,8,9]

for i in range(len(a)//2):
    x = a[i]
    y = a[0-1-i]
    temp = x
    a[i] = y
    a[0-i-1] = temp
    
print(a)

x = 7
y = 10

y = x+y
x = y-x
y = y-x

print(x,y)