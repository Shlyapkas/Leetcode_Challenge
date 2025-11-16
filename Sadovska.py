class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        lst = []
        greatest_amount = 0

        for i in candies:
            if i > greatest_amount: greatest_amount = i
        for i in candies:
            if i + extraCandies >= greatest_amount: lst.append(True)
            else: lst.append(False)

        return lst

s = Solution
print(s.kidsWithCandies(0, [1, 4, 7, 2], 3))
