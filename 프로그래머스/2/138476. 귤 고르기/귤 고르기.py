from collections import defaultdict

def solution(k, tangerine):
    answer = 0
    d = defaultdict(int)
    for x in tangerine:
        d[x] += 1
    l = sorted([d[x] for x in d], reverse=True)
    i = 0
    while k > 0:
        k -= l[i]
        i += 1
        answer += 1
    return answer