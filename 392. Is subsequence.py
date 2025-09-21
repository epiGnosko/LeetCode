class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        s_parser = 0
        for i in t:
            if i == s[s_parser]:
                s_parser += 1
            if s_parser == len(s):
                return True
        return False        
        