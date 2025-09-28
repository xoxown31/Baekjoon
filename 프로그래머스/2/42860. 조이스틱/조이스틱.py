def solution(s):
    a = sum(min(ord(c)-ord('A'), ord('Z')-ord(c)+1) for c in s)
    
    n = len(s)
    
    b = n - 1
    for i in range(n):
        j = i + 1
        while j < n and s[j] == 'A':
            j += 1
        b = min(2*i + n - j, i + 2*(n - j), b)
    
    return a + b