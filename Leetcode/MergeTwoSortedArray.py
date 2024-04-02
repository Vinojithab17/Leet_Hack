a = [2,3,5,6,7,8,9,11,23,55,77,78,99]
b = [2,34,5,6,3,6,7,7,522,33,444,5,6,63,366,477,3,7,443,88,5,322,799,9484]
b = list(set(b))
b.sort()
i = 0
j = 0
arr = []
while (i<len(a) and j<len(b)):
    if(a[i]==b[j]):
        arr.append(a[i])
        i+=1
        j+=1
    if a[i]>b[j]:
        arr.append(b[j])
        j = j+1
    elif a[i]<b[j]:
        arr.append(a[i])
        i = i+1
        
        
while(i<len(a)):
    arr.append(a[i])
    i +=1
while(j<len(b)):
    arr.append(b[j])
    j +=1
        
c = list(set(a+b))
c.sort()      
print(c)

print(arr)