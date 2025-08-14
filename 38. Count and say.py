class Solution:
    def countAndSay(self, n: int) -> str:
        def RLE(n: int) -> str:
            num = str(n)
            out = ""
            index = 0
            while index < len(num):
                currchar = num[index]
                count = 0
                while index < len(num) and currchar == num[index]:
                    count += 1
                    index += 1
                out += str(count) + str(currchar)
            return out 

        res = 1
        for _ in range(n-1):
            res = RLE(res)
        return str(res)