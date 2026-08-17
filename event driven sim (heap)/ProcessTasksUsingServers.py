import heapq

def assignTasks(servers: List[int], tasks: List[int]) -> List[int]:
    available = [(weight, i) for i, weight in enumerate(servers)]
    heapq.heapify(available)        
    busy = []
    time = 0
    m = len(tasks)
    ans = []

    for j, duration in enumerate(tasks):
        time = max(time, j)

        while busy and busy[0][0] <= time:
            _, weight, idx = heapq.heappop(busy)
            heapq.heappush(available, (weight, idx))
            
        if not available:
            # force all completions in this time stamp
            time = busy[0][0]
            while busy and busy[0][0] <= time:
                _, weight, idx = heapq.heappop(busy)
                heapq.heappush(available, (weight, idx))

        weight, idx = heapq.heappop(available)
        time_free = time + duration
        heapq.heappush(busy, (time_free, weight, idx))
        ans.append(idx)

    return ans

servers = list(map(int, input().split()))
tasks = list(map(int, input().split()))
print(assignTasks(servers, tasks))
