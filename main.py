from collections import Counter
#Binary Search
#from trie import *
# from linkedList import *
#from graph import *
#from tree import *
#from binaryTree import *
#from slidingWindow import *
#from longestCommonSubseq import *
#from heap import *
#from query import *
#from dfs import *
#from bfs import *
#from findAllLonelyNodes import *
from backTracking import *
#from matrix import *
#from logger import *
#from rearrange import *
#from kokobinary import *


#The maximum element closed to the search value
def KthMinElementSearch(li, k):
    left = 0
    right = len(li)
    print(f'{left} {right}')
    res = 0
    k = 17
    while (left <right):
        print(f'new left is {left}')
        print(f'new right is {right}')
        mid = left + (right-left) // 2
        print('mid value',mid,'value',li[mid])
        if (li[mid]<=k):
            res = max(res,mid) 
            left = mid+1 
        else:
             right = mid

    print('minimum ',li[res]) 
    return res


def search(li, num):
    left = 0
    right = len(li)-1
    print(f'{left} {right}')

    while (left <=right):
        print(f'new left is {left}')
        print(f'new right is {right}')
        mid = left + (right-left) // 2
        print('mid value',mid)
        print(li[mid])
        if li[mid]==num:
          print('found at index :',mid)
          return
        if (num >li[mid]):
            left = mid+1
         
        else:
            right = mid-1
            


li = [13, 22, 34, 42, 52,120]
#li = [1,2,3,4,5,6,7,8,9,10,11]
num = 52
# print(li)
# print(search(li,num))
# print(search(li,13))
# print(search(li,89))
# print(search(li,42))

#print(KthMinElementSearch(li,42))




class Animal:
    breed = None

    def __init__(self, sound):
        self.voice = sound
        Animal.breed = "Cat"
        self.__eat = "whiz"  #private
        self._run = "running"  #protected

    def shout(self):
        print(self.voice)
        print(Animal.breed)
        print(self.__eat)
        print(self._run)


# cat = Animal('Meow')
# cat.shout()
# print(Animal.breed)
# print(cat.eat)
# print(cat.run)
# words = ['abc','apple']
# adj = {char :set() for w in words for char in w}
# print(adj) # {'a': set(), 'b': set(), 'c': set(), 'p': set(), 'l': set(), 'e': set()}
# li = list(filter(lambda x: x <i, li))

# print('abc'in words)

# try :
#     # geeky_list = ["Geeky", "GeeksforGeeks", "SuperGeek", "Geek"]
#     # indices = [0, 1, "2", 3]
#     # for i in range(len(indices)):
#     #    print(geeky_list[indices[i]])
#     test = {'name':'akshit'}
#     print(test['sf'])
# except (KeyError,TypeError) as e:    
#     print(f'Error : {e.args[0]}')

#sorting
# jobs = sorted([(startTime[i], endTime[i], profit[i]) for i in range(len(startTime))], key=lambda x: x[0])

	
# dumy = [[1,3],[2,6],[8,10],[15,18]]
# dumy.sort()
# print(dumy)

string = "geeks for geeks"
print('Found at ',string.find('or'))

print(string.count('g'))


from itertools import permutations
 
def checkList(str, lst):
    #start from 2 letter perm
    for i in range(2, len(lst)+1):
        for perm in permutations(lst, i):
            if ''.join(perm)== str:
                return True
                 
    return False
     
# Driver code
str = 'geeks'
lst = ['for', 'ge', 'abc', 'ks', 'e', 'xyz']
#print(checkList(str, lst))

col = [2,4,4,5,5,1,2]
count = Counter(col)
#print(count)


def factorial(n):
    if n <=1:
      return 1
    return n*factorial(n-1)

#print(factorial(100))

main = ''
print(main=='')