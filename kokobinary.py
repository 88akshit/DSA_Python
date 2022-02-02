import math
class Solution:
    def minEatingSpeed(self, piles, h) -> int:
      
            def minSpeed(mid):
                maxi =0
                for  pile in piles:
                    maxi+= math.ceil(pile/mid)
                print('for mid point ',mid,'hours ',maxi)
                if maxi<=h:
                    return True
                else:
                    return False
        
            l = 1
            r=  max(piles)
            res=r
            while(l<r):
                print(f'looking in range l : {l} and r: {r}')
                mid = (l+r)//2             
                if minSpeed(mid):
                    print('found speed min',mid)
                    res = min(res,mid)
                    r= mid            
                else:
                    l= mid+1
            return res


#1,2,3,4,5,6,7,8,9,10,11


sol = Solution()
sol.minEatingSpeed([3,6,7,11],8)
