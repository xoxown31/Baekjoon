from math import gcd
from functools import reduce

def solution(arr):
    return reduce(lambda a,b:a*b//gcd(a,b), arr)