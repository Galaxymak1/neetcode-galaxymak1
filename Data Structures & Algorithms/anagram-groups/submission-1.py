class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = []
        dp = {}
        for word in  strs:
            key = "".join(sorted(word))
            if (key in dp.keys()):
                dp[key].append(word)
            else:
                dp[key] = [word]
        return [value for value in dp.values()]