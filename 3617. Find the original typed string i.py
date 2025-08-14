class Solution:
    def possibleStringCount(self, word: str) -> int:
        possibilities = 1
        start = 0
        till = 0
        while start < len(word):
            while till < len(word) and word[start] == word[till]:
                till += 1
            possibilities += till - start - 1
            start = till
        return possibilities