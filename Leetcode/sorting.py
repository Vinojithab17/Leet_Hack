class Solution:
    def sortColors(self, nums: list[int]) -> None:
        a=[0,0,0]
        nums2=[]
        for i in nums:
            if i ==0:
                a[0]+=1
            if i == 1:
                a[1]+=1
            if i == 2:
                a[2]+=1
        nums2 = [0]*a[0]+[1]*a[1]+[2]*a[2]
        for i in range(len(nums)):
            nums[i]=nums2[i]
        print(nums2)
        

        
        
c = Solution()

nums =[2,0,2,1,1,0]
c.sortColors(nums)