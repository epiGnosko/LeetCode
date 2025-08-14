class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_t = set(t)
        set_s = set(s)

        if len(set_s) != len(set_t):
            return False

        for char in set_t:
            if s.count(char) != t.count(char):
                return False
                break

        return True