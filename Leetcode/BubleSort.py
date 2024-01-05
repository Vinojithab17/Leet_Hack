a = [3,4,5,2,2,1,3,5,6,5,4,4,7,34,4,67,3,46,7,34,56,7,3,34,6]

# wrong way for implementing
# print("Length before sorting",len(a))
# for i in range(len(a)):
#     for j in range(len(a)-i -1):
#         if a[j]>a[j+1]:
#             a[j],a[j+1] = a[j+1],a[j]

           
# print("Length after sorting",len(a))
# print(a)


# optimized way for implementing
count = 0
swapped = True
while swapped:
    swapped = False
    for i in range(len(a)-1 - count):
        if a[i]>a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
            swapped = True
    count += 1
    if(not swapped):
        break
print(a)