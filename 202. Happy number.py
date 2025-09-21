class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n != 1:
            num = n
            n = 0
            while num:
                digit = num % 10
                n += digit * digit 
                num //= 10
            if n in visited:
                return False
            visited.add(n)

        return True