class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums)+1)]
        count = {}
        for i in nums:
            count[i] = count.get(i, 0)+1
        for i, v in count.items():
            freq[v].append(i)
        res = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k :
                    return res


            