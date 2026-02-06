# DFS solution
# string solution -> strings/GenerateParentheses.py
def generateParentheses(n: int) -> List[str]:
    ans = []
    def dfs(s, op, cl):
        # opened > closed -> can close
        # opened < N -> can open
        if len(s) == 2 * n:
            ans.append(s)

        if op < n:
            dfs(s + '(', op + 1, cl)

        if op > cl:
            dfs(s + ')', op, cl + 1)

    dfs('(', 1, 0)

    return ans

N = int(input())
print(generateParentheses(N))
