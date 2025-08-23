class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        def isSymmetric(i: int) -> int:
            x = i
            n = 0
            while x > 0:
                n += 1
                x //= 10
            if n % 2 == 1:
                return False
            sum1 = 0
            threshold = n / 2
            while n > threshold:
                sum1 += i % 10
                i //= 10
                n -= 1
            sum2 = 0
            while n > 0:
                sum2 += i % 10
                i //= 10
                n-=1
            return sum1 == sum2

        count = 0
        for i in range(low, high + 1):
            if isSymmetric(i):
                count += 1
        return count 