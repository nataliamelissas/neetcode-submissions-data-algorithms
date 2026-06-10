class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = 0
        total = 1

        for num in nums:
            if (num != 0):
                total *= num
            else:
                zeroCount += 1
                if (zeroCount >= 2):
                    total = 0
                    break # Results will always be 0, break early

        output = [0 for _ in nums]

        for i in range(len(nums)):
            if (zeroCount >= 2):
                return output
            elif (nums[i] == 0):
                newOut = total
            elif (zeroCount == 1):
                newOut = 0
            else:
                newOut = int(total / nums[i])
            
            output[i] = newOut

        return output