class TreeNode:
    def __init__(self):
        self.children={}
        self.endof=False
class Trie:
    def __init__(self):
        self.tempword=TreeNode()

    def insert(self, word: str) -> None:
        curr=self.tempword
        for c in word:
            if c not in curr.children:
                curr.children[c]=TreeNode()      
            curr=curr.children[c]
        curr.endof=True

    def search(self, word: str) -> bool:
        curr=self.tempword
        for c in word:
            if c not in curr.children:
                return False 
            curr=curr.children[c]
        return curr.endof     
        
    def startsWith(self, prefix: str) -> bool:
        curr=self.tempword
        for c in prefix:
            if c not in curr.children:
                return False      
            curr=curr.children[c]
        return True
        