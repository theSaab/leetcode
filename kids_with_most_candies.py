


def candy( candies, extraCandies ):
    m=max(candies)
    return [True if i+extraCandies>=m else False for i in candies]