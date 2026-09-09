class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        for i in range(len(flowerbed)):
            flower = flowerbed[i]

            if flower == 1:
                continue

            if (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                cnt += 1
                if cnt >= n:
                    return True
        return cnt >= n
