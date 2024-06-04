class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        i = 0
        j = 1
        count = 0
        while i< len(nums):
            if nums[i] == nums[j]:
                count +=1
                j+=1
            if j== len(nums):
                i +=1
                j = i+1
        