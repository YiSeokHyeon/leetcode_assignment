// https://leetcode.com/problems/convert-the-temperature

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        K= celsius+273.15
        F= celsius*1.80+32.00
        return [K,F]
        