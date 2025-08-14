class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        while max(digits) >= 10:
            for i in range(len(digits)):
                if digits[i] >= 10:
                    digits[i] %= 10
                    if i == 0:
                        digits = [1] + digits
                    else:
                        digits[i - 1] += 1
        return digits