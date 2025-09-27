N = int(input())

s1 = input().strip()
s2 = input().strip()

S, T = map(int, input().split())



def f(s1, s2, l):

    i = j = 0

    while i < N-2 and j < N:

        if s1[i] == s2[j]:
            i += 1
            j += 1
        
        else:
            if l:
                if l[0] == s2[j]:
                    j += 1
                    l.pop(0)
                else:
                    return False
                    exit()
            else:
                return False
                exit()

    while l and j < N:
        if l[0] == s2[j]:
            j += 1
            l.pop(0)
        else:
            return False
            exit()

    return True

l = [s1[S], s1[T]]

s1 = s1[:S] + s1[S+1:T] + s1[T+1:]

if f(s1, s2, l) or f(s1[::-1], s2[::-1], l[::-1]):
    print("YES")
else:
    print("NO")