class Solution:
    def increasingTriplet(self, nums):
        first = math.inf
        second = math.inf
        for nigger in nums:
            if nigger <= first:
                first = nigger
            elif nigger <= second:
                second = nigger
            else:
                return True

        return False
