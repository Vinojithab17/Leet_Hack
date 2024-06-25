class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        dic = {}
        dic2 = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = i
            else:
                if abs(dic[nums[i]]-i)<=k:
                    return True
                else:
                    dic[nums[i]] = i
        return False
s = Solution()
print(s.containsNearbyDuplicate([1],1))

# Wrong solution


