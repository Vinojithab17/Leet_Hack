class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        while n>0:
            if n==1:
                return True
            if n%3 ==0:
                # print(n)
                n = n//3
                print(n)

            else:
                return False
        return True
    
s = Solution()
print(s.isPowerOfThree(30))

print(1%3)