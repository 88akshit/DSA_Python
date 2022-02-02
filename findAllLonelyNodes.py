from binaryTree import *


#height of Tree
def dfs(root):
    if root is None:
      return 0
    return 1 + max(dfs(root.left),dfs(root.right))

def findLone(root):
    if root is None:
      return
    if (root.left is None and root.right) or (root.right is None and root.left):
      if root.left is None: li.append(root.right.data)
      if root.right is None: li.append(root.left.data)
     
    else:
      findLone(root.left)
      findLone(root.right)
    

li = []
dfs(findLone(getSampleRootNode()))

print(li)

