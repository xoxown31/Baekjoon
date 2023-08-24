from collections import defaultdict

def make_set(s):
    answer = defaultdict(int)
    for i in range(len(s)-1):
        if not (s[i].isalpha() and s[i+1].isalpha()):
            continue
        answer[(s[i]+s[i+1]).lower()] += 1
    return answer

def J(str1, str2):
    s1 = make_set(str1)
    s2 = make_set(str2)
    print(s1)
    print(s2)
    
    union = 0
    intersection = 0
    for e in s1:
        union += s1[e]
        if e in s2:
            intersection += min(s1[e], s2[e])
    
    for e in s2:
        union += s2[e]
    
    union -= intersection
    
    return intersection / union if union > 0 else 1

def solution(str1, str2):
    return int(J(str1, str2) * 65536)