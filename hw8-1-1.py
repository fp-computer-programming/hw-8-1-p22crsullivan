# Author: CRS 12/09/21
def totalpoints(freethrow, basketInside, basketBeyond):
    totalPoints = 0
    totalPoints = (freethrow * 1) + (basketInside * 2) + (basketBeyond * 3)
    return totalPoints


print(totalpoints(3, 2, 0))

print(totalpoints(5, 1, 0))

print(totalpoints(1, 0, 0))
