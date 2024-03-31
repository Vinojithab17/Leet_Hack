digits = [4,3,2,1]
x = 0
y = []
for i in range(len(digits)):
    x += digits[i]*(10**(len(digits)-i-1))
x+=1

while x > 0:
    y.append(x%10)
    x = x//10
    
    
print(y[::-1])

