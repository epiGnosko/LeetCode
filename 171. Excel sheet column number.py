class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        if columnTitle == "":
            return 0
        return 26*(self.titleToNumber(columnTitle[:-1])) + ord(columnTitle[-1]) - 64