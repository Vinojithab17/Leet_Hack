print("Hello World")

nums = [-1,0,1,2,-1,-4]
nums = [0,0,0]



def twoSum(nums,target)-> list[int]:

    c = {}
    for i in nums:
        c[i] = i

    for i in range(len(nums)):
            if target- nums[i] in c and i != nums.index(target- nums[i]) and i!=nums.index(-target) and nums.index(-target)!=nums.index(target- nums[i]) :
            # if target- nums[i] in c and i != nums.index(target- nums[i]) :
                return [-target ,nums[i] , target- nums[i]]
       
# for i in range(len(a)):
    
for i in range(len(nums)-2):
     target = nums[i]
     print(twoSum(nums,-target))

# print(set([-1, 0, 1]) == set([0, -1, 1]))