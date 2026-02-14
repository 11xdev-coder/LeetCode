from collections import defaultdict

def prefixConnected(words: List[str], k: int) -> int:
    prefixes = defaultdict(int)

    for word in words:
        if len(word) < k:
            continue
            
        i = 0
        prefix = []
        while i < k:
            prefix.append(word[i])
            i += 1

        prefixes["".join(prefix)] += 1

    ans = 0
    for i, (key, value) in enumerate(prefixes.items()):
        if value > 1:
            ans += 1
    return ans

words = list(input().split())
k = int(input())
print(prefixConnected(words, k))
