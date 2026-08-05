def corpFlightBookings(bookings: List[List[int]], n: int) -> List[int]:
    diff = [0] * (n+1)
    for l, r, v in bookings:
        diff[l-1] += v
        diff[r] -= v

    result = []
    running = 0
    for num in diff:
        running += num
        result.append(running)

    return result[:-1]

bookings = []

while True:
    line = input()
    if not line:
        break
    
    row = list(map(int, line.split()))
    bookings.append(row)

n = int(input())
print(corpFlightBookings(bookings, n))
