// https://leetcode.com/problems/number-of-good-pairs

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]==nums[j]:
                    n+=1
        n=(n-len(nums))/2
        return int(n)
    