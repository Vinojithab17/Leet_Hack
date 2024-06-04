

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        i = 0
        j = 0
        x = {}
        while i < len(digits):
            k = int(digits[i]) + 45
            a = chr(ord(digits[i])+k+j + k-47)
            print(a)
            j+=1
            if j==3:
                i+=1
                j=0


s  = Solution()
s.letterCombinations('32')