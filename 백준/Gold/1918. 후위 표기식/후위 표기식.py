priority = {
    '+':1,
    '-':1,
    '*':2,
    '/':2
}

infix = input().strip()

postfix = ""

stack = []
for c in infix:
    if c.isalpha():
        postfix += c
    elif c == '(':
        stack.append(c)
    elif c == ')':
        while stack[-1] != '(':
            postfix += stack.pop()
        stack.pop()
    else:
        if not stack:
            stack.append(c)
        else:
            while stack and stack[-1] != '(' and priority[c] <= priority[stack[-1]]:
                postfix += stack.pop()
            stack.append(c)

while stack:
    postfix += stack.pop()

print(postfix)
