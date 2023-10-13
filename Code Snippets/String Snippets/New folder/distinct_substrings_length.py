
#using Trie

class TrieNode:
    def __init__(self):
        self.child=[None for i in range(26)]
        self.isword=False

def count_substrings(string):
    head=TrieNode()
    count=[]
    for i in range(len(string)):
        t=head
        p=0
        for j in range(i,len(string)):
            if not t.child[ord(string[j])-ord('a')]:
                t.child[ord(string[j])-ord('a')]=TrieNode()
                t.isword=True
                p+=1

            t=t.child[ord(string[j])-ord('a')]
        count.append(p)
    return count


if __name__=="__main__":
    s=input()
    print(count_substrings(s))
