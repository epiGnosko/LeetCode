class Solution:
    def intToRoman(self, num: int) -> str:
        conversion = {
            1   : "I",
            5   : "V",
            10  : "X",
            50  : "L",
            100 : "C",
            500 : "D",
            1000: "M"
        }
        arr = []
        place = 1
        while num > 0:
            arr.append(num % 10 * place)
            num //= 10
            place *= 10
        ans = ""
        for place in arr[::-1]:
            first = int(str(place)[0])
            if first == 0:
                continue
            elif first in (1, 5):
                ans = ans + conversion[place]
            elif first < 4:
                ans = ans + conversion[place // first] * first
            elif first == 4:
                pre = place // 4 * 5
                post = place // 4
                ans = ans + conversion[post] + conversion[pre]
            elif first < 9:
                base = place * 5 // first
                ans = ans + conversion[base] + conversion[(place - base) // (first - 5)] * (first - 5)
            elif first == 9:
                ans = ans + conversion[place // 9] + conversion[place * 10 // 9]
                
        return ans 
                

        