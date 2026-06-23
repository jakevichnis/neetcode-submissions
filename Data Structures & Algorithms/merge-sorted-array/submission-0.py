class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        right = 0
        output = ""
        for i in range(len(nums1[m:])):
            nums1[m + i] = nums2[right]
            right += 1 


        nums1.sort()
        