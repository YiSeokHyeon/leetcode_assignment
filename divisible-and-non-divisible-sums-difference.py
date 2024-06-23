// https://leetcode.com/problems/divisible-and-non-divisible-sums-difference

class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1=0
        num2=0
        for i in range(1,n+1,1):
            if i % m !=0:
                num1+=i
        for j in range(1,n+1,1):
            if j % m ==0:
                num2+=j
        return num1-num2        