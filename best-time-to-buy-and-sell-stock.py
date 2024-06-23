// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    sellOne = 0
    holdOne = -math.inf

    for price in prices:
      sellOne = max(sellOne, holdOne + price)
      holdOne = max(holdOne, -price)

    return sellOne