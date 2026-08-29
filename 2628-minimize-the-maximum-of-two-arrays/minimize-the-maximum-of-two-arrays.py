class Solution(object):
    def minimizeSet(self, divisor1, divisor2, uniqueCnt1, uniqueCnt2):

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def possible(x):
            lcm = divisor1 * divisor2 // gcd(divisor1, divisor2)

            # Numbers usable by arr1 and arr2
            a1 = x - x // divisor1
            a2 = x - x // divisor2

            # Numbers usable by both arrays
            common = x - x // divisor1 - x // divisor2 + x // lcm

            # Enough numbers for each array,
            # and enough total distinct numbers
            return (a1 >= uniqueCnt1 and
                    a2 >= uniqueCnt2 and
                    x - x // lcm >= uniqueCnt1 + uniqueCnt2)

        left = 1
        right = 2 * (uniqueCnt1 + uniqueCnt2)

        while left < right:
            mid = (left + right) // 2

            if possible(mid):
                right = mid
            else:
                left = mid + 1

        return left