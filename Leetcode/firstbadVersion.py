def isBadVersion(version: int) -> bool:
    if version>=4 : return True
    else: return False

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 0
        high = n
        mid = (low+high)//2
        minVal = n
        while minVal!=mid:
            if isBadVersion(mid)==False:
                low = mid
                mid = (low + mid)//2

            if isBadVersion(mid):
                if mid<minVal:
                    minVal = mid
                    high = minVal
                    mid = (low + high)//2

                else :
                    high = minVal
                    mid = (low + high)//2
        print(minVal)
s = Solution()
s.firstBadVersion(10)