class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        jump1 = 3
        jump2 = 2
        ans = 0

        for _ in range(n-3):
            ans = jump1 + jump2
            jump2 = jump1
            jump1 = ans

        return ans