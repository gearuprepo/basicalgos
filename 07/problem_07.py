
# A RouteTrieNode will be similar to our autocomplete TrieNode... 
# with one additional element, a handler.
class RouteTrieNode:
    def __init__(self,handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, path):
        # Insert the node as before
        if path not in self.children:
            self.children[path] = RouteTrieNode()

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, 
        # this is the root path or home page node
        self.root = RouteTrieNode()

    def insert(self, route, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) 
        # node of this path
        current_node = self.root
        if route == '/':
            self.root.handler = handler
        else:
            splitpaths = route.split("/")
            for path in splitpaths:
                if path !='':
                    current_node.insert(path)
                    current_node = current_node.children[path]
            current_node.handler = handler

    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        splitpaths = path.split("/")
        current_node =self.root
        for p in splitpaths:
            if p!='':
                if p not in current_node.children:
                    return False
                current_node = current_node.children[p]
        return current_node.handler

rt = RouteTrie()
rt.insert("/home/about","Handler about")
rt.insert("/home/","Handler home")
rt.insert("/","root Handler")
rt.insert("/me","me handler")
print(rt.find("/about/"))
print(rt.find("/"))