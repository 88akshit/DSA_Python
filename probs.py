import List

def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashSet = {}
        for num in range(0,len(numbers)):
            ans = target -numbers[num]
            if ans in hashSet:
                return [hashSet[ans],num+1]
            else:
                hashSet[numbers[num]] = num+1

def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i , a in enumerate(nums):
            if i>0 and a ==nums[i-1]:
                continue
            l,r = i+1,len(nums)-1
            while l<r:
                threesum = a+nums[l]+nums[r]
                if(threesum > 0):
                    r-=1
                elif(threesum < 0):
                    l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    while nums[l]== nums[l-1] and l<r:
                        l+=1
        return res