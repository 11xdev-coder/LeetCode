def mapWordWeights(words: List[str], weights: List[int]) -> str:
    ans = []
    for word in words:
        weight = 0
        for c in word:
            weight += weights[ord(c) - ord('a')]
        idx = 25 - weight % 26
        ans.append(chr(idx + ord('a')))

    return "".join(ans)

words = list(input().split())
weights = list(map(int, input().split()))

print(mapWordWeights(words, weights))
