class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        corres = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
        }
        for i in s:
            if i in "[{(":
                stack.append(i)
            elif stack == []:
                return False
            elif stack[-1] == corres[i]:
                stack.pop(-1)
            else:
                return False
        return stack == []
        