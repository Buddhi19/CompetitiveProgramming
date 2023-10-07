"""
Trie data structure for insert and 
search for a word in a trie
"""

class TrieNode:
    def __init__(self) -> None:
        self.children={}
        self.isend=False

class Trie:
    def __init__(self) -> None:
        self.root=self.getNode()
        self.autocomp_ans=[]

    def getNode(self):
        return TrieNode()
    
    def insert(self,key):
        parent=self.root
        for level in key:
            if not parent.children.get(level):
                parent.children[level]=self.getNode()
            parent=parent.children[level]

        parent.isend=True

    def search(self,key):
        parent=self.root
        for level in key:
            if not parent.children.get(level):
                return False
            parent=parent.children[level]

        return parent.isend
    
    def autocomp(self,node,word):
        if node.isend:
            self.autocomp_ans.append(word)
        
        for a,n in node.children.items():
            self.autocomp(n,word+a)

    def list_suggestions(self,key):
        parent=self.root
        self.autocomp_ans=[]
        for level in key:
            if not parent.children.get(level):
                return 0
            parent=parent.children[level]
        
        if not parent.children:
            return -1
        self.autocomp(parent,key)
        return self.autocomp_ans


def word_splitting(words:list,name:str):
    """
    check whether a given string can be breaked down to given keys
    """
    t=Trie()
    n=len(name)
    for i in range(len(words)):
        t.insert(words[i])
    if n==0:
        return True
    for i in range(1,n+1):
        if t.search(name[:i]) and word_splitting(words,name[i:]):
            return True
    return False

def autocomplete():  
    """
    autocomplete
    """
    t=Trie()

    keys=["hello", "dog", "hell", "cat", "a",
            "hel", "help", "helps", "helping"] 
    for key in keys:
        t.insert(key)

    print(t.list_suggestions("h"))

if __name__=="__main__":
    words=["hello", "dog", "hell", "cat", "a",
            "hel", "help", "helps", "helping"]
    print(word_splitting(words,"heldog"))