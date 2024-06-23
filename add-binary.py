// https://leetcode.com/problems/add-binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
       A=int(a, 2)
       B=int(b, 2)
       N=A+B
       pre=bin(N)[2:]
       ans=str(pre)
       return ans
