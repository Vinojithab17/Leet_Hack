a = [1,2,3,4,5,6,7,8,9]

def findIndex(nums,n):
    mid = len(nums)//2
    if nums[mid] ==n:
        return mid
    else:
        if nums[mid] >n:
            return findIndex (nums[:mid],n)
        else: return findIndex(nums[mid+1:],n)

print(findIndex(a,8))

def findValue(nums,n):
    low = 0
    high = len(nums)-1
    while low<=high:
        mid = (high+low)//2
        if nums[mid] == n:
            return mid
        else:
            if nums[mid] > n:
                high = mid-1
            else: low  = mid+1
    return -1


print(findValue(a,8))
                
