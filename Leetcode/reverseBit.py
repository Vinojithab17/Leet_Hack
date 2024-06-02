class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = ''
        l = len(n)
        num = 0
        for i in range(l):
            num += int(n[i])*2**(i)
            reverse = n[i] + reverse
        print(num,reverse)

n = '00000010100101000001111010011100'

sol = Solution()
sol.reverseBits(n)
        
a = 43261596

print(len(bin(a)[2:]))