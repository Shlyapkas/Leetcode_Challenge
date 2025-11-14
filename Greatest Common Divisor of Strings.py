class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return "-"
        elif str1 == str2:
            return str1
        else:
            needed = ""
            less = min(str1, str2)
            bigger = max(str1, str2)
            for i in range(1, len(less)+1):
                prefix = less[:i]
                if len(less) % i == 0 and len(bigger) % i == 0:
                    if prefix * (len(less) // i) == less and prefix * (len(bigger) // i) == bigger:
                        needed = prefix
            return needed


s = Solution

print(s.gcdOfStrings(0, "ABABAB", "ABAB"))