class Solution:
    def addDigits(self, num: int) -> int:
        sum = 0
        while True:
            if num==0 and sum <10:
                print(sum)
                return sum
            elif num == 0 and sum>=10:
                print(sum)
                num = sum
                sum = 0
            else:
                sum += num%10
                num  = num//10

sol = Solution()
sol.addDigits(38)


        