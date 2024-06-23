// https://leetcode.com/problems/projection-area-of-3d-shapes

class Solution:
  def projectionArea(self, grid: List[List[int]]) -> int:
    return sum(a > 0 for row in grid for a in row) + sum(max(row) for row in grid) + sum(max(col) for col in zip(*grid))