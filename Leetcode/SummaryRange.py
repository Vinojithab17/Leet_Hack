class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if len(nums)<= 1:
            return [str(nums[0])]
        else:
            l = []
            dic={}
            j = 1
            i = 0
            num1 = 0
            num2 = 0
            while j<len(nums):
                num1 = nums[i]
                num2 = nums[j-1]
                if nums[j] - nums[j-1] ==1:
                    j +=1
                    if j ==len(nums):
                        dic[num1] = nums[j-1]
                        l.append('{n}->{b}'.format(n=num1,b=nums[j-1]))
                else:

                    if num1 !=num2:
                        l.append('{n}->{b}'.format(n=num1,b=num2))
                    else: l.append(str(num1))
                    i = j 
                    j +=1
                    if j == len(nums):
                        l.append(str(nums[i]))

            print(dic)
            print(l)

s = Solution()
print(s.summaryRanges([1]))
