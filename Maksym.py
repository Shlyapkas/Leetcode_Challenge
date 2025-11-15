class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = list(map(lambda x: x + extraCandies >= max(candies), candies))
        return result
