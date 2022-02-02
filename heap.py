import heapq


def max_heapify(arr,n,i):
    largest = i
    left = 2*i+1
    right = 2*i+2
    if left < n and arr[largest]<arr[left]:
      largest = left
    if right<n and arr[largest]<arr[right]:
      largest = right
    if largest !=i:
      arr[i],arr[largest] = arr[largest],arr[i]
      max_heapify(arr,n,largest)

def min_heapify(arr,n,i):
    smallest = i
    left = 2*i+1
    right = 2*i+2
    if left < n and arr[smallest]>arr[left]:
      smallest = left
    if right<n and arr[smallest]>arr[right]:
      smallest = right
    if smallest !=i:
      arr[i],arr[smallest] = arr[smallest],arr[i]
      min_heapify(arr,n,smallest)

arr = [2,15,4,30,18,6,25]
n = len(arr)
print("len",n)
for i in range(n//2-1,-1,-1):
  print("index",i)
  max_heapify(arr,n,i)
  #min_heapify(arr,n,i)

print('Max Heap is')
for i in range(n):
  print(arr[i])

#       2
#   15      4
#30  18  6   25


dummyList = [5,7,9,1,3]
heapq.heapify(dummyList)
print(dummyList)
heapq.heappush(dummyList,90)
print(dummyList)
heapq.heappop(dummyList)
print(dummyList)

print(heapq.nlargest(2,dummyList))
print(heapq.nsmallest(2,dummyList))


# Max Heap with -1 Insert-O(Logn) , getMax O(1)
heap = []
heapq.heapify(heap)
  
# Adding items to the heap using heappush
# function by multiplying them with -1
heapq.heappush(heap, -1 * 10)
heapq.heappush(heap, -1 * 30)
heapq.heappush(heap, -1 * 20)
heapq.heappush(heap, -1 * 400)
  
# printing the value of maximum element
print("Head value of heap : "+str(-1 * heap[0]))

# printing the elements of the heap
print("The heap elements : ")
for i in heap:
    print(-1 * i, end = ' ')
print("\n")
  
element = heapq.heappop(heap)
  
# printing the elements of the heap
print("The heap elements : ")
for i in heap:
    print(-1 * i, end = ' ')