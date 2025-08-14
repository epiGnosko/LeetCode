class Solution:
    def makeFancyString(self, s: str) -> str:
        fancystring = s[:2]
        for i in s[2:]:
            if i != fancystring[-1] or i != fancystring[-2]:
                fancystring += i
        return fancystring

        