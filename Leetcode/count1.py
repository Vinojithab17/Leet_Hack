a = {'1':0,'0':0}
b = bin(2147483645)
print(b)
for i in range(2,len(b)):
    a[b[i]] += 1

print(a['1'])