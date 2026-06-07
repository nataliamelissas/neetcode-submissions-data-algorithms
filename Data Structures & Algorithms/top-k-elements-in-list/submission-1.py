import heapq
from operator import itemgetter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # get amounts
        intAmounts = {}

        # find the frequencies
        for i in range(len(nums)):
            amount = intAmounts.get(nums[i])
            if amount is None:
                amount = 0 # start fresh
            
            amount = amount + 1
            intAmounts.update({nums[i]: amount})

        # create frequency buckets
        freq = [[] for _ in range(len(nums) + 1)]
        for n, c in intAmounts.items():
            freq[c].append(n)

        answer = []
        for idx in reversed(range(len(nums) + 1)):
            answer.extend(freq[idx])
            if (len(answer) >= k):
                return answer[:k]

        # add to a max heap but instead of just sorting by largest, i get the nlargest or klargest using heapq.nlargest...
        #top_k = heapq.nlargest(k, intAmounts.items(), key=itemgetter(1))
        #return [key for key, value in top_k] # used list comprehension to flatter/map to only the keys

        # test
        #print(intAmounts)
        #return list(intAmounts.values())