def solution(absolutes, signs):
    return sum(x * (1 if sign else -1) for x, sign in zip(absolutes, signs))