flowerbed = [0, 0, 1, 0, 1]
n = 0
class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        count = 0
        if n == 0:
            return True
        else:
            for i in range(1, len(flowerbed)-1):
                if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    count += 1

                    if count >= n:
                        return True
        return count >= n
s = Solution()
print(s.canPlaceFlowers(flowerbed, n))
