import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i] = 1 
        for i in dic:
            dic[i] = -dic[i]

        min_heap= []
        for key,val in dic.items():
            heapq.heappush(min_heap,(val,key))
        ans = []
        for i in range(k):
           (x,y) =  heapq.heappop(min_heap)
           ans.append(y)
        return ans
        

        

        