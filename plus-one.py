// https://leetcode.com/problems/plus-one

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = ''.join(map(str, digits))  # 리스트의 각 숫자를 문자열로 변환하여 연결
        N = int(n) + 1  # 숫자에 1을 더한 후
        p = str(N)  # 다시 문자열로 변환
        ans = list(map(int, p))  # 각 자리의 숫자를 리스트에 넣어서 반환
        return ans
