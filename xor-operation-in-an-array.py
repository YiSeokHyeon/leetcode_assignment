// https://leetcode.com/problems/xor-operation-in-an-array

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        l=0
        for i in range(n):
            a=start+2*i
            l=l^a
        
        return l
