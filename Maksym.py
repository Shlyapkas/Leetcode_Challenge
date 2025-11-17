class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.insert(0, 0)
        flowerbed.append(0)
        flowerbed.append(1)
        counter = 0
        zero_num = 0
        for i in flowerbed:
            if not i:
                zero_num += 1
            else:
                counter += (zero_num / 2 - 0.5) // 1
                zero_num = 0
        return counter >= n
