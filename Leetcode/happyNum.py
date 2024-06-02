class Solution:
    def isHappy(self, n: int) -> bool:
        n = 19
        sum = 0
        for i in range(100):
            if n == 0 and sum == 1:
                return True
                break
            else:
                if n==0:
                    n = sum
                    print(n)
                    sum = 0

            sum += (n%10)**2
            n = n//10
        return False
S = Solution()
print(S.isHappy(2))