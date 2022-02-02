class Node:
  def __init__(self, data, next ):
    self.data = data
    self.next = next

class LinkedList:

  def __init__(self):
    self.head = None

  def insertAtBegin(self, data):
      newNode = Node(data,self.head)
      self.head = newNode

  def print(self):     
      if self.head is None:
         print('Linked List is Empty')
         return
      itr = self.head
      listStr = ''
      while itr:
          listStr+=str(itr.data)+'-> '
          itr = itr.next
      print(listStr)

  def insertAtBack(self,data):
      if self.head is None:
         self.head = Node(data,None)
         return
      itr = self.head
      while itr.next:
            itr = itr.next
      itr.next = Node(data,None)

num = LinkedList()
num.insertAtBegin(40)
num.insertAtBegin(30)
num.insertAtBack(90)
num.print()