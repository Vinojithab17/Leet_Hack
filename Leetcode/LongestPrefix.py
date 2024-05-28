class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        a = 1
        b = ''
        c = len(strs)

        d = strs[0]
        if len(d)==0:
            return d
        i = 0
        if c == 1:
            return strs[0]
        while(i < c-1 and a<=len(d)):
            b = strs[0][:a]
            if b != strs[i+1][:a]:
                b = b[:a-1]
                break
            if b == strs[i+1][:a]:
                i+=1
            if i == c-1:
                i=0
                a+=1
        return b
    
solution = Solution()

strs = ["flower", "flow", "flight"]
strs = ["flower","flower","flower","flower"]

print(solution.longestCommonPrefix(strs))  # Output should be "fl"
    
