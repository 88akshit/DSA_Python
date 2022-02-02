from collections import Counter
import heapq

class Solution:
    def rearrange(self,s,k):
        counter = Counter(s)
        print(counter)
        #pq = [(counter[c],c) for c in counter] # min Heap
        pq = [(-(counter[c]),c) for c in counter] # max heap add -1
        print(pq)
        heapq.heapify(pq)
        # print(heapq.nlargest(1, pq))
        # print(heapq.nsmallest(1, pq))
        # heapq.heappop(pq)
        #heapq.heappush(pq,(-10,'e'))
        print(pq)
        #print(heapq.heappop(pq)[0])
        res = ''
        while len(pq)>1:
            curr = heapq.heappop(pq)
            next = heapq.heappop(pq)

            res+=curr[1]
            res+=next[1]
            print(curr[0]+1)
            if curr[0]+1!=0:
              heapq.heappush(pq,(curr[0]+1,curr[1]))
            if next[0]+1!=0:
              heapq.heappush(pq,(next[0]+1,next[1]))
            print(pq)
            print(res)
        if len(pq)>0:
            last = heapq.heappop(pq)
            if last[0]!=-1:
              return ''
            res+=last[1]


        print(res)



sol = Solution()
s= 'vvvlo'
k=3
sol.rearrange(s,k)