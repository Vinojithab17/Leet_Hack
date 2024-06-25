class Solution:
    def countBits(self, n: int) -> list[int]:
        a = []
        for i in range (n+1):
            a.append(self.countOne(i))
        return a
    def countOne(self,num):
        count=0
        for i in bin(num):
            if i  =='1':
                count+=1
        return count


s = Solution()   
print(bin(2)[2:])
print(s.countBits(5))
print(14**0.5)
print(14//(14**0.5))

