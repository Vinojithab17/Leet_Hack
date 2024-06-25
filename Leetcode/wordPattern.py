class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        dic2 = {}
        a = s.split(' ')
        ans2 = ''
        if len(a)!=len(pattern):
            return False
        
        for i in range(len(pattern)):
            dic[pattern[i]] = a[i]
            dic2[a[i]] = pattern[i]
            ans2 +=a[i]
        ans=''
        pattern2 = ''
        for i in range(len(pattern)):
            ans += dic[pattern[i]] 
            pattern2 += dic2[a[i]]
        if ans == ans2 and pattern == pattern2:
            return True
        else : return False

pattern = "abba"
a = "dog cat cat dog"
s  = Solution()
print(s.wordPattern(pattern,a))