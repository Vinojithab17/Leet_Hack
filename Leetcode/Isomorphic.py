class Solution:
    def counter(self, t: str,)-> list[int]:
        a = []
        count = 1
        prev = t[0]
        for i in t[1:]:
            if i == prev:
                count+=1
                prev = i
            else:
                prev = i
                a.append(count)
                count = 1
        a.append(count)
        return a
    def isIsomorphic(self, s: str, t: str) -> bool:
        a = {}
        b = {}
        for i in range(len(s)):
            if s[i] in b:
                b[s[i]] += 1
            else:
                b[s[i]] = 1

            if t[i] in a:
                a[t[i]]  += 1  
            else:
                a[t[i]] = 1  
        k = 0
        print(a,b)
        for i in range(len(s)):
            if a[t[i]] == b[s[i]] :
                continue
            else:
                return False
        return True and self.counter(s)==self.counter(t)
        

s = "badc"
t = "baba"


sol = Solution()


print(sol.isIsomorphic(s,t))

print(bin(16))
print(bin(32))
print(bin(1))
print(bin(3))