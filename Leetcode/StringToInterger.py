class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if s =="" :
            return 0
        sign = ''
        if s[0] == '-' or s[0] ==  '+':
            sign = s[0]
            s = s[1:]
        for i in s:
            if i.isdigit():
                sign += i
            else: break
        if sign == '-' or sign == '+' or sign == '': return 0
        else : 
            
            if int(sign)< -2**31:
                return -2**31
            elif int(sign)> 2**31-1:
                return 2**31-1
            else : return int(sign)