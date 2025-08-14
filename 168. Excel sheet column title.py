class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphas = [columnNumber - 1]
        while alphas[0] > 25:
            alphas = [alphas[0] // 26 - 1] + alphas
            alphas[1] = alphas[1]%26
        print(alphas)
        ans = ""
        for i in alphas:
            ans += chr(i + 65)
        return ans
        