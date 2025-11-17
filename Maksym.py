class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0,1]
        counter, zero_num = 0, 0
        for i in flowerbed:
            if not i:
                zero_num += 1
            else:
                counter += (zero_num / 2 - 0.5) // 1
                zero_num = 0
        return counter >= n
