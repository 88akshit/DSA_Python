class BinarySearchTreeNode:
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
                 self.left = BinarySearchTreeNode(data)
          else:
              if self.right:
                  self.right.add_child(data)
              else:
                 self.right = BinarySearchTreeNode(data)

      def in_order_traversal(self):
          element = []
          if self.left:
            element+=self.left.in_order_traversal()
          element.append(self.data)
          if self.right:
            element+=self.right.in_order_traversal()
          return element

      

      def search(self,val):
        if self.data == val:
          return True
        elif val < self.data:
            if self.left:
              return self.left.search(val)
            else:
              return False
        elif val > self.data:
            if self.right:
              return self.right.search(val)
            else:
              return False

      def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

      def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements

     
      
      def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

      def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

      def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum
      
def leftView(root,level,elements,maxLevel):
    if root.data is None:
      return []
    else:
      if maxLevel< level:
        elements.append(root.data)
        print(elements)
        maxLevel = level
    leftView(root.left, level+1,elements,maxLevel)
    leftView(root.right,level+1,elements,maxLevel)
    return elements

def build_tree(element):
    root = BinarySearchTreeNode(element[0])
    for i in range(1,len(element)):
        root.add_child(element[i])
    return root

def in_order_iter(root):
    stack = []
    result = []
    while root is not None or stack !=[]:
        while root is not None:
            stack.append(root)
            root = root.left
        root = stack.pop()
        result.append(root.data)
        root = root.right
    return result

def preorderTraversal(root):
      stack = [root]
      result = []
      while stack!=[]:
          root = stack.pop()
          result.append(root.data)
          if root.right:
              stack.append(root.right)
          if root.left:
              stack.append(root.left)
      return result

def postorderTraversal(root):
    stack = [root]
    result = []
    while stack!=[]:
        root = stack.pop()
        result.append(root.data)
        if root.left:
            stack.append(root.left)
        if root.right:
            stack.append(root.right)
    print(result)
    return result[::-1]

#numbers = [17,4,1,20,9,23,18,24]
numbers = [1,2,3]
numbers_tree = build_tree(numbers)
#print(in_order_iter(numbers_tree))
print(preorderTraversal(numbers_tree))
print(leftView(numbers_tree,1,[],0))
#print(postorderTraversal(numbers_tree))
# print(numbers_tree.in_order_traversal())
# print(numbers_tree.post_order_traversal())
# print(numbers_tree.search(180))



