import math
a, b, v = map(int, input().strip().split())
print(int(math.ceil((v-a)/(a-b)) + 1))