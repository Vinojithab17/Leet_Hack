x = -1234
b = 0
c = abs(x)
if x < 0:
    a = -1
else : 
    a =1
while c > 0:
    b = b*10 + c%10
    c = c//10
print(b*a)