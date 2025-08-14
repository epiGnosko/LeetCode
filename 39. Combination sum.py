class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, combination, target_left):
            if target_left == 0:
                result.append(combination.copy())
                return
            if target_left < 0:
                return

            for i in range(start, len(candidates)):
                combination.append(candidates[i])
                backtrack(i, combination, target_left - candidates[i])
                combination.pop()

        backtrack(0, [], target)
        return result
            