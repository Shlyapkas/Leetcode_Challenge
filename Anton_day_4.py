def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    for index in range(len(flowerbed)):
        if flowerbed[index] == 1:
            continue
        else:
            if index == 0:
                if len(flowerbed) == 1:
                    n -= 1
                    flowerbed[index] = 1
                elif flowerbed[index + 1] == 0:
                    n -= 1
                    flowerbed[index] = 1
            elif flowerbed[index - 1] == 0:
                if index == len(flowerbed) -1:
                    n -= 1
                    flowerbed[index] = 1
                else:
                    if flowerbed[index + 1] == 0:
                        n -= 1
                        flowerbed[index] = 1
    if n <= 0:
        return True
    else:
        return False

flowerbed = [1,0,0,0,1]
n = 1
canPlaceFlowers(flowerbed, n)