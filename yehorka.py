extraCandies = 5
candies = [2, 3, 7, 1, 3]
class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxCandies = max(candies)
        output = []
        for kid in candies:
            if kid + extraCandies >= maxCandies:
                output.append(True)
            else:
                output.append(False)

        return output
s = Solution()
print(s.kidsWithCandies(candies, extraCandies))
