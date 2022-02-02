class TreeNode:
    def __init__(self,data):
      self.data = data
      self.children = []
      self.parent = None

    def addChildren(self,child):
      self.children.append(child)
      child.parent= self
    
    def getLevel(self):
      l = 0
      p = self.parent
      while p:
          l+=1
          p=p.parent
      return l

    def printTree(self):
      space = ' '*self.getLevel()*3
      print(space+'|_'+self.data)
      if self.children:
        for child in self.children:
            child.printTree()


      

def buildProductTree():
  root =TreeNode('Devices')

  monitor = TreeNode('Monitor')
  monitor.addChildren(TreeNode('LG'))
  monitor.addChildren(TreeNode('Samsung'))
  monitor.addChildren(TreeNode('Benq'))


  root.addChildren(TreeNode('Mouse'))
  root.addChildren(TreeNode('Keyboard'))
  root.addChildren(monitor)

  root.printTree()
  return root

buildProductTree()

