import heapq

def getOrder(tasks: List[List[int]]) -> List[int]:
    tasks = [(enqueue, process, i) for i, (enqueue, process) in enumerate(tasks)]
    tasks.sort()
        
    available = []
    i = 0
    time = 0
    ans = []

    while i < len(tasks) or available:
        # -> available
        while i < len(tasks) and tasks[i][0] <= time:
            # lowest processing time first, then idx
            heapq.heappush(available, (tasks[i][1], tasks[i][2]))
            i += 1

        if not available:
            time = tasks[i][0]
            continue

        processingTime, idx = heapq.heappop(available)
        ans.append(idx)
        time += processingTime

    return ans

