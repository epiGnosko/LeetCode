class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counters = []
        for i in range(len(strs)):
            counters.append({})
            for char in strs[i]:
                if char in counters[i]:
                    counters[i][char] += 1
                else:
                    counters[i][char] = 1
        ans = []
        while strs != []:
            currhash = counters[0]
            indices = []
            group = []
            index = 0
            while index < len(strs):
                if counters[index] == currhash:
                    indices.append(index)
                index += 1
            for i in sorted(indices, reverse=True):
                group.append(strs.pop(i))
                counters.pop(i)
            ans.append(group.copy())
        return ans