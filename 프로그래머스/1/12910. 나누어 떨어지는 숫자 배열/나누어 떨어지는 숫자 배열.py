def solution(arr, divisor):
    l = sorted([x for x in arr if x%divisor == 0])
    return l if l else [-1]