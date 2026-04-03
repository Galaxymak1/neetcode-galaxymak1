class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = []
        dp = {}
        for word in  strs:
            key = "".join(sorted(word))
            dp[key] = {}
            for l in word :
                if l in dp[key].keys():
                    dp[key][l] +=1 
                else:
                    dp[key][l] = 1
        for i,word in enumerate(dp.keys()):
            results.append([])
            for wd in strs:
                if "".join(sorted(wd)) == word :
                    results[i].append(wd)
        return results