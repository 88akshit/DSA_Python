maxLevel = 0

class BinaryTreeNode:
      def __init__(self,data):
          self.data = data
          self.left = None
          self.right = None

      def add_child(self,data):
          if data == self.data:
            return
          elif data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
              self.left = BinaryTreeNode(data)
          else:
            if self.right:
                self.right.add_child(data)
            else:
              self.right = BinaryTreeNode(data)


def build_tree(element):
    root = BinaryTreeNode(element[0])
    for i in range(1,len(element)):
        root.add_child(element[i])
    return root

      
def leftView(root,level,elements):
    global maxLevel
    if root is None:
      return elements
    else:
      if maxLevel< level:
        # print(root.data)
        # print(root.left)
        # print(root.right)
        elements.append(root.data)
        # print(elements)
        print('level value',maxLevel)
        maxLevel = level
    leftView(root.left, level+1,elements)
    leftView(root.right,level+1,elements)
    return elements

def searchDFS(root,key):
    found = False
    if root is None:
      return
    if root.data ==key:
      return True
    if root.left:
      found = searchDFS(root.left,key)
    if root.right and found != True:
      found = searchDFS(root.right,key)
    return found

def getSampleRootNode():
    numbers = [5,2,8,7]
    return build_tree(numbers)

numbers = [5,2,8,7,12]
numbers_tree = build_tree(numbers)
#print(searchDFS(numbers_tree,7))
print(leftView(numbers_tree,1,[]))