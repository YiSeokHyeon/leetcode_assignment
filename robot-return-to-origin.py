// https://leetcode.com/problems/robot-return-to-origin

class Solution:
  def judgeCircle(self, moves: str) -> bool:
    return moves.count('R') == moves.count('L') and moves.count('U') == moves.count('D')