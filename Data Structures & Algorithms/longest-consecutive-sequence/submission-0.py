class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        long = 0
        for r in nums:
            if r-1 not in numset:
                length = 1
                while r+length in numset:
                    length+=1
                long = max(length, long)
        return long
