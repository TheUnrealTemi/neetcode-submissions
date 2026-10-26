class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            cur_max = max(cur_max + nums[i], nums[i])

            max_sum = max(max_sum, cur_max)

        return max_sum