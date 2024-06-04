class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        a = {}
        i = 0
        j = 0
        m =''
        while i<26:
            if key[i]==' ':
                continue
            if key[i] not in a:
                a[key[i]]  = chr(i+97)
                i+=1
                j+=1
            else:
                j+=1 
        for i in message:
            if i ==' ':
                m+=i
            else :
                m+=a[i]
        print(a)
        print(m)

key = "eljuxhpwnyrdgtqkviszcfmabo"
message = "zwx hnfx lqantp mnoeius ycgk vcnjrdb"
s = Solution()
s.decodeMessage(key,message)
