class Solution:
    def maximum69Number (self, num: int) -> int:
        x = str(num)
        ans = x
        for i in range(len(x)):
            if x[i] == "6":
                ans = x[:i] + "9" + x[i+1:]
                break
        return int(ans)
        