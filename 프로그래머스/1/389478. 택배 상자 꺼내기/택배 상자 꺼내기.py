def solution(n, w, num):
    answer = (n-1) // w - (num-1) // w + 1
    x1 = (n-1)%w
    x2 = (num-1)%w
    if ((n-1)//w)%2 == ((num-1)//w)%2:
        if x1 < x2:
            print("Case 1")
            answer -= 1
    else:
        if x1 + x2 < w-1:
            print("Case 2")
            answer -= 1
    return answer