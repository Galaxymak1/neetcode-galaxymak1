class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dp = {}
        for num in nums:
            if num in dp.keys():
                return True
            else :
                dp[num] = 1
        return False