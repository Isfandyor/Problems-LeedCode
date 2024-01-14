import math
area=int(input())
sqrt = int(math.sqrt(area))
while sqrt > 0 and area % sqrt != 0:
    sqrt -= 1
length = area // sqrt
print([length, sqrt])





