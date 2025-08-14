class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = [0]
        power = 0
        mod = 10**9 + 7
        while n > 0:
            if n & 1 == 1:
                powers.append(powers[-1] + power)
            n = n >> 1
            power += 1
        powers.pop(0)
        ans = []
        # for left, right in queries:
        #     result = powers[right]
        #     if left != 0:
        #         result -= powers[left - 1]
        #     result = (1 << result) % mod
        #     ans.append(result)
        ans = [((1 << (powers[right] - (powers[left - 1] if left > 0 else 0))) % mod) for left, right in queries]
        return ans