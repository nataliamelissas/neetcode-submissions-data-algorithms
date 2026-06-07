import heapq
from operator import itemgetter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # get amounts
        intAmounts = {}

        for i in range(len(nums)):
            amount = intAmounts.get(nums[i])
            if amount is None:
                amount = 0 # start fresh
            
            amount = amount + 1
            intAmounts.update({nums[i]: amount})

        # add to a max heap
        top_k = heapq.nlargest(k, intAmounts.items(), key=itemgetter(1))
        return [key for key, value in top_k]

        # test
        #print(intAmounts)
        #return list(intAmounts.values())