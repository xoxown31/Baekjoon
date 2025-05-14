def solution(brown, yellow):
    for i in range(brown):
        for j in range(brown):
            if 2 < i <= j and i * 2 + j * 2 == brown + 4 and (i-2) * (j-2) == yellow:
                return [j, i]