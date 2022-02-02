
arr = [1,9,-1,-2,7,3,-1,2]
k = 4
n = len(arr)
print(n)
maxSum = 0
windowSum = 0
for j in range(0,k):
    windowSum = windowSum + arr[j]

for i in range(k,n):
  windowSum = windowSum +arr[i] - arr[i-k]
  maxSum = max(windowSum, maxSum)
print("Sum",maxSum)


