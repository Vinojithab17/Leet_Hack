print("Hello World")

a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
b = 20

c = {}

for i in range(len(a)):
    c[a[i]] = a[i]


for i in a:
    try:
        # print(c[abs(b-i)])
        if a.index(i) != a.index(abs(b-i)) : print(a.index(i),a.index(abs(b-i))) 
    except ValueError as e :
        continue

# for i in range(len(a)):
    
print(c)

