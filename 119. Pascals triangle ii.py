class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(rowIndex):
            for i in range(1, len(row)):
                row[i-1] = row[i] + row[i-1]
            row = [1] + row
        return row