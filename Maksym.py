class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
            if str1 * len(str2) != str2 * len(str1):
                return ""
            primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
            comps1 = []
            num1 = len(str1)
            comps2 = []
            num2 = len(str2)
            for i in primes:
                while num1 % i == 0:
                    comps1.append(i)
                    num1 /= i
                while num2 % i == 0:
                    comps2.append(i)
                    num2 /= i
            mults = []
            for i in comps1:
                if i in comps2:
                    mults.append(i)
                    comps2.remove(i)
            fin_len = 1
            for i in mults:
                fin_len *= i
            return str1[:fin_len]
