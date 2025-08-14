class Solution:
    def largestGoodInteger(self, num: str) -> str:
        curr = ""
        i = 0
        while i < len(num)-2:
            if num[i] == num[i+1] == num[i+2]:
                if curr == "" or curr[0] < num[i]:
                    curr = num[i:i+3]
                i += 3
            elif num[i+1] == num[i+2]:
                i += 1
            else:
                i += 2
        return curr
        