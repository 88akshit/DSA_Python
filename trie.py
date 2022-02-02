class Node:
  def __init__(self):
        self.children = {}
        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class Trie:
  def __init__(self):
        self.root = Node()
  
  def print(self):
      pCrawl = self.root
      print(pCrawl.children['t'].children)
      for letter in pCrawl.children:
        print(letter)

      

    

  def insert(self,word):
         
      # If not present, inserts key into trie
      # If the key is prefix of trie node,
      # just marks leaf node
      pCrawl = self.root
      for letter in word:
        if letter not in pCrawl.children:
            pCrawl.children[letter] = Node()
        pCrawl = pCrawl.children[letter]
      
      pCrawl.isEndOfWord = True
  
  def search(self,word):
         
      # If not present, inserts key into trie
      # If the key is prefix of trie node,
      # just marks leaf node
      pCrawl = self.root
      for letter in word:
        if letter not in pCrawl.children:
          return False
        pCrawl = pCrawl.children[letter]

      if pCrawl.isEndOfWord:
        return True
      else:
        return False

 


    


keys = ["the","there",'akshit']


t = Trie()
for key in keys:
    t.insert(key)
t.print()
print(t.search('there'))