class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if  nums == [0]* (len(nums)) :
            return nums
        if Counter(nums)[0] >1:
            return [0]*len(nums)
        res_without = 1
        res_with = 1
        for i in nums:
            res_with *=i 
            if i !=0:
                res_without *=i 
        ans = []
        if res_with == res_without:
            for i in nums:
                ans.append(int(res_without/i))
            return ans
        else:
            for i in nums:
                if i ==0:
                    ans.append(res_without)
                else:
                    ans.append(0)
            return ans


