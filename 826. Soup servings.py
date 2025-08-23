class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1.00000
        memo = {}
        def count_paths(a, b, n):
            if (a, b) in memo:
                return memo[(a, b)]

            factor = 0.25**n

            # tuple is (a_first, both_same_time, total)
            if a <= 0 and b <= 0:
                return (0, factor, factor)
            if a <= 0:
                return (factor, 0, factor)
            if b <= 0:
                return (0, 0, factor)

            res_a = 0
            res_both = 0
            res_total = 0
            for da, db in [(100, 0), (75, 25), (50, 50), (25, 75)]:
                temp_a, temp_both, temp_total = count_paths(a - da, b - db, n + 1)
                res_a += temp_a
                res_both += temp_both
                res_total += temp_total

            memo[(a, b)] = (res_a, res_both, res_total)
            return memo[(a, b)]

        a_first, both, total = count_paths(n, n, 0)
        return (a_first + 0.5 * both) / total