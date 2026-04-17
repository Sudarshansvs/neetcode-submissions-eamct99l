class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        pf = [0]
        for n in nums:
            pf.append(pf[-1] + (1 if n==0 else 0))
        res =0 
        for l in range(len(nums)):
            low, h = l, len(nums)
            while low<h:
                mid = (low+h)//2
                if pf[mid+1] - pf[l]<=k:
                    low = mid+1
                else:
                    h = mid
            res = max(res, low-l)
        return res
                