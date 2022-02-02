data = [[1,2,3],[4,5,6]]

def printMatrix(data):
  for row in data:
      for elem in row:
          print(elem, end=' ')
      print()

def inputData(a,data):
  n = 0
  #length of row
  for i in range(len(a)):
    #print("i",i)
    #length of column
    for j in range(len(a[i])):
      #print(f'value of i {i} and j {j}')
      n+=2
      a[i][j] = n

# DFS recursion
def dfs(r,c):
    
    if r<0 or c<0 or r==3 or c==4:
      return 0
    
    if a[r][c] == 1:
       a[r][c] = 0
    dfs(r+1,c)
    # dfs(r-1,c)
    dfs(r,c+1)
    #dfs(r,c-1)
    #print(a)

r = 3
c = 4
#a = [[0 for x in range(c)] for y in range(r)]
a = [[0, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1]]
print(a)
#inputData(a,data)
printMatrix(a)
dfs(0,0)
print('Result')
printMatrix(a)
