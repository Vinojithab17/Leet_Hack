def guess(num: int) -> int:
    g = 3
    if num>g: return -1
    if num < g : return 1
    if num == g : return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n+1
        num = (low+high)//2
        while(True):
            print(num)
            if guess(num)==0:
                return num
            elif guess(num)==1:
                low = num
            else:
                high = num
            num = (low+high)//2

s = Solution()

s.guessNumber(3)
