# string solution
# DFS solution -> dfs/GenerateParantheses.py
def solve(n: int) -> List[str]:
    def open(arr, pair, op, cl):
        pair_copy = pair[::]
        pair_copy.append("(")
        arr.append((pair_copy, op+1, cl))
    def close(arr, pair, op, cl):
        pair_copy = pair[::]
        pair_copy.append(")")
        arr.append((pair_copy, op, cl+1))
        
    cur_pairs = [(["("], 1, 0)]

    while len(cur_pairs[0][0]) < 2*n:
        added = []
        for cur_pair in cur_pairs:

            pair, opened, closed = cur_pair
            if opened > closed:
                if opened < n:
                    open(added, pair, opened, closed)
                close(added, pair, opened, closed)
            else:
                open(added, pair, opened, closed)

            cur_pairs = added[::]

    ans = []
    for (pair, op, cl) in cur_pairs:
        ans.append("".join(pair))

    return ans

N = int(input())
print(solve(N))
