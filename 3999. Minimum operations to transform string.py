class Solution:
    def minOperations(self, s: str) -> int:
        minchar = s[0]
        for i in s:
            if minchar == 'a' and i != 'a':
                minchar = i
            if i < minchar and i != 'a':
                minchar = i
        if minchar == 'a':
            return 0
        return 26 - (ord(minchar) - ord('a'))