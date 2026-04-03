from operator import itemgetter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dp = {}
        for num in nums :
            dp[num] = 1 + dp.get(num,0)
        sorted_dp = dict(sorted(dp.items(),key=itemgetter(1)))
        return list(sorted_dp.keys())[-k:]