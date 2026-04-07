class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = []
        sm_max = 0
        for i in range(len(arr)-1):
            sm_max = max(arr[i+1:])
            ans.append(sm_max)
        ans.append(-1)
        return ans
