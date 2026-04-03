from operator import itemgetter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dp = {}
        for num in nums :
            if num in dp.keys():
                dp[num] += 1
            else :
                dp[num] = 1
        sorted_dp = dict(sorted(dp.items(),key=itemgetter(1)))
        return list(sorted_dp.keys())[-k:]