class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for j in range(len(nums)):
            for i in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    if i>j:
                        return [j,i]
                    else:
                        return [i,j]
        return [0,0]
