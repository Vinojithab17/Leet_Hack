from decimal import Decimal, getcontext
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        getcontext().prec = 20
        list1 = []
        i = 0 
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i]> nums2[j]:
                list1.append(nums2[j])
                j+=1
            else:
                list1.append(nums1[i])
                i+=1
        while i < len(nums1):
            list1.append(nums1[i])
            i+=1

        while j < len(nums2):
            list1.append(nums2[j])
            j+=1

        print(list1)

        count = len(list1)
        if count%2:
            result = Decimal(list1[count//2]) / Decimal(1)
            formatted_result = result.quantize(Decimal('1.00000'))
            print(formatted_result)
        else:
            result = Decimal(list1[count//2-1] + list1[count//2]) / Decimal(2)
            formatted_result = result.quantize(Decimal('1.00000'))
            print(formatted_result)
            # print(("{:.5f}".format((list1[count//2-1] + list1[count//2])/2.00000,5)))

c = Solution()
l1 = [100000]
l2 = [100001]
c.findMedianSortedArrays(l1,l2)