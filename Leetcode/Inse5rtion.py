a = [3,4,5,2,2,1,3,5,6,5,4,4,7,34,4,67,3,46,7,34,56,7,3,34,6]

for i in range(1 , len(a)):
    key = a[i]
    j = i-1
    
    while j>=0 and a[j]> key:
        a[j+1] = a[j]
        j -= 1
    a[j+1] = key
    
print(a)




