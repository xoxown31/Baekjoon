import sys

input = sys.stdin.readline

N = int(input())

link = {}

for _ in range(N):
    node, left, right = input().split()
    link[node] = (left, right)

def preorder(word):
    if word == '.':
        return

    print(word, end = '')
    preorder(link[word][0])
    preorder(link[word][1])

def inorder(word):
    if word == '.':
        return

    inorder(link[word][0])
    print(word, end = '')
    inorder(link[word][1])

def postorder(word):
    if word == '.':
        return

    postorder(link[word][0])
    postorder(link[word][1])
    print(word, end = '')

preorder('A'); print();
inorder('A'); print();
postorder('A'); print();
