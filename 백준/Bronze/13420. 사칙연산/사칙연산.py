import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    I = input().split('=')
    if eval(I[0]) == eval(I[1]):
        print("correct")
    else:
        print("wrong answer")
    
