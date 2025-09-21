class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        def helper(digits: str, letterkeeping: dict, ans: List[str]) -> List[str]:
            if digits == "":
                return ans
            newans = []
            for i in ans:
                for newletter in letterkeeping[digits[0]]:
                    newans.append(i + newletter)
            return helper(digits[1:], letterkeeping, newans)

        letterkeeping = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz",
        }
        ans = [""]
        ans = helper(digits, letterkeeping, ans)
        return ans
