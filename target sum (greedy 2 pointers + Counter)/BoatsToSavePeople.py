def numRescueBoats(people: List[int], limit: int) -> int:
    people.sort()

    low, high = 0, len(people) - 1
    boats = 0
    while low <= high:
        if people[low] + people[high] <= limit:
            low += 1
        high -= 1
        boats += 1

    return boats

people = list(map(int, input().split()))
limit = int(input())
print(numRescueBoats(people, limit))
