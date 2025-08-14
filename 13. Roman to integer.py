class Solution:
    def romanToInt(self, s: str) -> int:
        val = 0
        valmap = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        prev = 0
        for i in s[::-1]:
            if valmap[i] >= prev:
                val += valmap[i]
            else:
                val -= valmap[i]
            prev = valmap[i]
        return val



        