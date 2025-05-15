def solution(n, words):
    s = set([words[0]])
    for i, word in enumerate(words[1:]):
        if words[i][-1] != word[0] or word in s:
            return [(i+1)%n+1, (i+1)//n+1]
        s.add(word)
    return [0, 0]