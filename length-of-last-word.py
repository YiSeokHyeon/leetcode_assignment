// https://leetcode.com/problems/length-of-last-word

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        set=s.split()
        N=len(set)
        n=len(set[N-1])
        return n