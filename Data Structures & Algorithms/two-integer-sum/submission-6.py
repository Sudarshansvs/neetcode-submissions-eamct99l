class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if target-nums[i] ==nums[j]:
        #             return [i,j]
        for i in range(len(nums)):
            x = target-nums[i]
            if x in nums[i+1:]:
                for j in range(i+1, len(nums)):
                    if x == nums[j]:
                        return [i,j]
            
                
            