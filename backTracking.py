class Solution:
    def permutations(self,num):
        result = []
        #Base Condition
        if len(num)==1:
            return [num.copy()]
        for n in num:
          popElem = num.pop(0)
          #Relation
          per = self.permutations(num)
          #print(per)
          for p in per:
              p.append(popElem)
      
          result.extend(per)
          num.append(popElem)
        return result

    def backTrack(self,nums):
        strSet = [s for s in nums]
        print(strSet)
        combo= []
        def backTracking(i,curr):
            print(curr," ",i)
            if i ==2:
                res = "".join(curr)
                if res not in strSet:
                  combo.append(res)
                #return None
                return None if res in strSet else res

            
            res = backTracking(i+1,curr)
            if res:
                return res
            curr[i] = "1"
            res = backTracking(i+1,curr)
            curr[i]=  "0"
            if res:
                return res
            
        print(backTracking(0,["0" for n in range(2)]))
        combo.extend(strSet)
        print(combo)

  
sol = Solution()
#num = [1,2,3]
num = ['A','B','C']
word = 'ship is big'
percob = word.split(' ') # ['ship', 'is', 'big']
#percob = [char for char in word] #['s','h']

#print(sol.permutations(num))

# for item in sol.permutations(num):
#     res.append("".join(item))
# print(res)

res = ["".join(item) for item in sol.permutations(num)]
#print(res)

sol.backTrack(["11","10",'00'])    

# for n in range(0,3,2):
#   print(num[n])

class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []
        for ele in tokens:
            print(ele)
            if str(ele) !='*' or str(ele) !='+' or str(ele) !='-' or str(ele) !='\\':
                stack.append(ele)
            else:
                ele1 = stack.pop()
                ele2 = stack.pop()
                if ele =='*':
                    res = ele1*ele2
                    stack.append(res)
                elif ele =='+':
                    res =ele1+ele2
                    stack.append(res)
                elif ele =='-':
                    res =ele1-ele2
                    stack.append(res)
                elif ele =='/':
                    res =ele1/ele2
                    stack.append(res)
        return stack[0]
