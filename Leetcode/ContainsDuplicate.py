class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        ans = []
        for i in range(len(nums)):
            if nums[i] == k:
                ans.append(i)
        print(ans)
        if len(ans)>=2:
            if (ans[1]-ans[0]<=k):
                return True
        if len(ans)==1 :
            return True
        else: return False

s = Solution()
print(s.containsNearbyDuplicate([1,0,1,1],1))

# Wrong solution


