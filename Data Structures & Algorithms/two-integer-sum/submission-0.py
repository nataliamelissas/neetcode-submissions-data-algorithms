class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx1, val1 in enumerate(nums):
            if idx1 == (len(nums) - 1):
                print("exiting")
                return
            for idx2, val2 in enumerate(nums[idx1 + 1:], start=idx1 + 1):
                twoSum = val1 + val2
                if twoSum == target:
                    return [idx1, idx2]
