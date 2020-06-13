# Autocomplete with tries

class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}
    
    # O(n) = n
    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.children:
            self.children[char] = TrieNode()
    
    # O(n) = nlogn
    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for 
        ## all complete words below this point
        retarr = []
        for key in self.children:
            self.recur(self.children[key],suffix+key,retarr)
        return retarr
            
    def recur(self,node,suffix,retarr):
        if len(node.children) == 0:
            return suffix
        else:
            if node.is_word:
                retarr.append(suffix)
            for key in node.children:
                val = self.recur(node.children[key],suffix+key,retarr)
                if val != None:
                    retarr.append(val)

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    
    # O(n) = n*m,  n- no of chars, m-no of children
    def insert(self, word):
        current_node = self.root
        for char in word:
            current_node.insert(char)
            current_node = current_node.children[char]
        current_node.is_word = True

    # O(n) = n * m, n- no of chars, m-no of children
    def find(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", "fact",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')

f('ant')
f('f')
f('z')
f('tri')