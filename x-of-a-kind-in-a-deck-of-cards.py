// https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards

class Solution:
  def hasGroupsSizeX(self, deck: List[int]) -> bool:
    count = collections.Counter(deck)
    return functools.reduce(math.gcd, count.values()) >= 2
    