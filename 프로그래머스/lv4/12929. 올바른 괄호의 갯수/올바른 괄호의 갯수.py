from itertools import permutations
from math import factorial

def solution(n):
    return (factorial(2*n) // (n+1)) // factorial(n) ** 2