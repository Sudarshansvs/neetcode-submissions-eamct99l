class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        final_lne = len(nums)
        for i in range(final_lne):
            nums.append(nums[i])
        return nums

        