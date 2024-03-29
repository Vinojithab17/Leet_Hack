a = [1,2,3,3,1,3,4,9,45,5,6,64,3,6,7,5,4,7]

a.sort()
# print(a[0])
# print(a.index(a[4]))
# print(a.index(45))

# def removeDuplicates(nums):
#     arr = []
#     b = len(nums)
#     for i in range(b):
#         if nums.index(nums[i]) == i:
#             arr.append(nums[i])

#     for i in range(b - len(arr)):
#         arr.append(-1111111)
#     c = len(arr)
#     nums = arr
#     return c
# list(set(a)).sort()
# print(list(set(a)))



def removeDuplicates2(nums):
    count = 0   
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            nums[i] = 1000
            count = count + 1
    nums.sort()
    print(nums[:len(nums)-count])
    return len(nums[:len(nums)-count])

print(removeDuplicates2(a))