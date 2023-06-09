def kidsWithCandies(candies, extraCandies):
    res = []
    for x in candies:
        if x + extraCandies >= max(candies):
            res.append(True)
        else:
            res.append(False)
    return res

candies = [2,3,5,1,3]
extraCandies = 3

print(kidsWithCandies(candies, extraCandies))
