class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i] = nums2[i]
        # print(nums1)
        #[10, 20, 20, 40, 1, 2]
        #divide the nums1 into 2 parts m and n 
        return nums1.sort()

        