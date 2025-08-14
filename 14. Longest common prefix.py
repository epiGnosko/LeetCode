class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        index = 0
        longestprefix = ""
        minlen = len(strs[0])
        for i in strs:
            if len(i) < minlen:
                minlen = len(i)
        while index < minlen:
            char = strs[0][index]
            for i in strs:
                if i[index] != char:
                    return longestprefix
            longestprefix += char
            index += 1
        return longestprefix

        