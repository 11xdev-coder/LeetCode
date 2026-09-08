# brute force
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1 = len(str1)
        l2 = len(str2)

        def validate(n: int) -> bool:
            base = str1[:n]
            c1 = l1 // len(base)
            c2 = l2 // len(base)
            
            if base * c1 == str1 and base * c2 == str2:
                return True
            return False

        for length in range(min(l1, l2), 0, -1):
            if validate(length):
                return str1[:length]
        return ""

# GCD
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        gcd = math.gcd(len(str1), len(str2))
        return str1[:gcd]
        
