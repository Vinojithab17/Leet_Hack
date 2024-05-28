a = [1,2,3,4,5,6,6,7,8]
b = [1,2,3,4,5,6,6,7,8]

for i in range(len(a)//2):
    temp = a[i]
    a[i] = a[-1-i]
    a[-1-i] = temp
    # a[i],a[-1-i] = a[-1-i],a[i]

# print(a)


k = 3

# print(b[-3:]+b[:len(b)-3])


nums = [1,2,3,4,5,6,7]
k = 3
for i in range(len(nums)//2):
    nums[i],nums[-i-1] = nums[-i-1],nums[i]

for i in range(k):
    p = nums.pop(0)
    nums.append(p)


for i in range(len(nums)//2):
    nums[i],nums[-i-1] = nums[-i-1],nums[i]

print(nums)


