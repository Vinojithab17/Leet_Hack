class Solution:
    def toHex(self, num: int) -> str:

        if num == 0:
            return '0'
        if num<0:
            num = 2**32 + num
        l = {
        0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 
        6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 
        11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'
        }
        hexa = ''
        while num>0:
            hexa = l[num%16] + hexa
            num  = num//16
        
        return  hexa 
        


s = Solution()
print(s.toHex(26))

print(ord('1')-48)
print(ord('9')-48)


n = "123"
num=0
for i in range(len(n)):
    num += (ord(n[len(n)-1-i])-48)*10**i
print(num)