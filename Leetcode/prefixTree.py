class Node:
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word 
        self.end = False
  
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=Node()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr=self.root

        for i in range(len(word)):
            index= ord(word[i])-97
            if not curr.children[index]:
                curr.children[index]=Node()
            curr=curr.children[index]
        curr.end=True
        


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr=self.root
        #found=False
        
        l = len(word)
        for i in range(l):
            index= ord(word[i])-97
            if not curr.children[index]:
                return False
            curr=curr.children[index]
        if curr != None and curr.end:
            return True

        


    def startsWith(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr=self.root
        #found=False
        
        l = len(word)
        for i in range(l):
            index= ord(word[i])-97
            if not curr.children[index]:
                return False
            curr=curr.children[index]
        
        if curr != None:
            return True
        
        

def main():
    t= Trie()
    t.insert("apple")
    t.insert("app")
    t.insert("ba")
    t.insert("back")

    print(t.search("apple"))
    print(t.search("ba"))
    print(t.search("all"))
    print(t.startsWith("back"))
    print(t.search("bak"))
    print(t.startsWith("ba"))

if __name__ == '__main__':
    main()

