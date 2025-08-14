class Solution:
    def isValid(self, word: str) -> bool:
        vowel = False
        consonant = False
        for i in word:
            if i.lower() in "aoeui":
                vowel = True
            elif i.lower() in "pyfgcrldhtnsqjkxbmwvz":
                consonant = True
            elif i in "7531902468":
                continue
            else:
                return False
        return len(word) > 2 and vowel and consonant