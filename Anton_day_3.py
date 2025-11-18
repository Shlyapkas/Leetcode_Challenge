def kidsWithCandies(candies: list[int], extraCandies: int) -> list[bool]:
    maximum = max(candies)
    result = []
    for item in candies:
        if item + extraCandies >= maximum:
            result.append(True)
        else:
            result.append(False)

    return result


candies = [4,2,1,1,2]
extraCandies = 1

print(kidsWithCandies(candies, extraCandies))