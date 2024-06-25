class Solution:
    def isUgly(self, n: int) -> bool:
        n = abs(n)
        for i in range(2,n):
            if self.isPrime(i) and i > 5 and n%i==0:
                return False
        return True
    
    def isPrime(self,n):
        if(n <= 1):
            return False
        for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    

s = Solution()
print(s.isUgly(14))
        