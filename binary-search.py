// https://leetcode.com/problems/binary-search

class Solution:
  def search(self, nums: List[int], target: int) -> int:
    i = bisect.bisect_left(nums, target)
    return -1 if i == len(nums) or nums[i] != target else i