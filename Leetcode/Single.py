a = [1,2,2]

b = {}
for i in a:
    try:
        b[i] +=1
    except KeyError:
        b[i] = 1

print(len(b))
for i in b:
    if b[i] ==1:
        print (i)