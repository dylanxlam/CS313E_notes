class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return nums[0] if nums[0] > nums[1] else nums[1]

        def dp(i, nums, cache):
            # base case
            if i >= len(nums)-2 and i < len(nums):
                return nums[i]
            if i >= len(nums)-1:
                return 0
            # cache
            if i in cache:
                return cache[i]

            rob_next_2 = dp(i+2, nums, cache)
            rob_next_3 = dp(i+3, nums, cache)

            max_n = max(rob_next_2, rob_next_3)
            cache[i] = max_n + nums[i]

            return max_n + nums[i]

        cache = {}
        
        return max(dp(0, nums, cache), dp(1, nums, cache))

            