import copy
class Solution:
    def reorderedPowerOf2(self, number: int) -> bool:
        legals = {}
        n = 1
        while n <= 10**9:
            subdict = {}
            num = str(n)
            subdict["len"] = len(num)
            subdict["count"] = {}
            for i in num:
                if i not in subdict["count"]:
                    subdict["count"][i] = 1
                else:
                    subdict["count"][i] += 1
            legals[n] = copy.deepcopy(subdict)
            n *= 2
        
        n_str = str(number)
        count = {}
        for i in n_str:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        print(count)
        for i in legals:
            if len(n_str) != legals[i]["len"]:
                continue
            if count == legals[i]["count"]:
                print(legals[i]["count"])
                return True

        return False