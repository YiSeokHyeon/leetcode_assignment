// https://leetcode.com/problems/valid-perfect-square

class Solution:
  def isPerfectSquare(self, num: int) -> bool:
    l = bisect.bisect_left(range(num), num,
                           key=lambda m: m * m)
    return l**2 == num