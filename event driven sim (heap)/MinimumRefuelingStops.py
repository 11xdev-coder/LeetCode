import heapq

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        passed = []
        ans = 0
        prev_dist = 0

        stations.append([target, float('-inf')])
        for dist, fuel in stations:
            startFuel -= dist - prev_dist

            while passed and startFuel < 0:
                startFuel += -heapq.heappop(passed)[0]
                ans += 1
            
            if startFuel < 0:
                return -1

            heapq.heappush(passed, (-fuel, dist))
            prev_dist = dist

        return ans
