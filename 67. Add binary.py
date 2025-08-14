class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            b = '0'*(len(a)-len(b)) + b
        elif len(a) < len(b):
            a = '0'*(len(b)-len(a)) + a
        res = ""
        index = -1
        carry = False
        while index >= -len(a):
            if a[index] != b[index]:
                if carry:
                    res = '0' + res
                    carry = True
                else:
                    res = '1' + res
                    carry = False
            else:
                if a[index] == '0':
                    if carry:
                        res = '1' + res
                        carry = False
                    else:
                        res = '0' + res
                        carry = False
                else:
                    if carry:
                        res = '1' + res
                        carry = True
                    else:
                        res = '0' + res
                        carry = True
            index -= 1
        if carry:
            res = '1' + res
        return res