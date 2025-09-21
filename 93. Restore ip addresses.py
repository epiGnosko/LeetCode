class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        out = []
        for i in range(1,4):
            for j in range(i+1, i+4):
                for k in range(j+1, j+4):
                    ip = s[:i] + "." + s[i:j] + "." + s[j:k] + "." + s[k:]
                    nums = ip.split(".")
                    valid = True
                    print(ip)
                    for l in nums:
                        if l == "":
                            valid = False
                            break
                        if l[0] == "0" and len(l) > 1:
                            valid = False
                            break
                        if int(l) > 255:
                            valid = False
                            break
                    if valid:
                        out.append(ip)
        return out 