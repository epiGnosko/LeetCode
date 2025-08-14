class Solution:
    def myAtoi(self, s: str) -> int:
        out = 0
        neg = False
        index = 0
        if s == "":
            return out 
        while index < len(s) and s[index] == " ":
            index += 1
        if index < len(s) and s[index] == "-":
            neg = True
            index += 1
        elif index < len(s) and s[index] == "+":
            index += 1
        while index < len(s) and s[index] in "1234567890":
            out = out * 10 + int(s[index])
            index += 1
        if neg:
            return max(-2**31,-out)
        return min(2**31 - 1,out)
            
            
            
        