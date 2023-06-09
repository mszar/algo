def kidsWithCandies(candies, extraCandies):
    return [True if _ + extraCandies >= max(candies) else False for _ in candies]

candies = [2,3,5,1,3]
extraCandies = 3

print(kidsWithCandies(candies, extraCandies))
