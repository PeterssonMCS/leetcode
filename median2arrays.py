class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = nums1+nums2
        nums3.sort()
        i = int(len(nums3)/2)
        
        if (int(len(nums3)) % 2 == 0):
            return (nums3[i-1]+nums3[i])/2
        else:
            return nums3[i]
