class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dp = {}
        for num in nums :
            dp[num] = 1 + dp.get(num,0)
        sort_array = []
        for num,cnt in dp.items():
            sort_array.append((cnt,num))
        sort_array.sort()
        result = []
        while len(result) < k:
            result.append(sort_array.pop()[1])
        return result