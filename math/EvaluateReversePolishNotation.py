import math

def evalRPN(tokens: List[str]) -> int:
    stack = []

    # each operation we look at 2 previous nums and calculate it
    # replace them with new result
    for token in tokens:
        match token:
            case '+':
                res = stack.pop() + stack.pop()
                stack.append(res)
            case '-':
                second = stack.pop()
                first = stack.pop()
                res = first - second
                stack.append(res)
            case '*':
                res = stack.pop() * stack.pop()
                stack.append(res)
            case '/':
                second = stack.pop()
                first = stack.pop()
                res = math.trunc(first / second)
                stack.append(res)
            case _:
                stack.append(int(token))

    return stack[0]

tokens = list(input().split())
print(evalRPN(tokens))
