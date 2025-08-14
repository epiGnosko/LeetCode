class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for _ in range(numRows):
            if ans == []:
                ans.append([1])
                continue
            nextrow = [1]
            for i in range(len(ans[-1])-1):
                nextrow.append(ans[-1][i] + ans[-1][i+1])
            nextrow.append(1)
            ans.append(nextrow[:])
        return ans