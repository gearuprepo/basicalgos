
class RouteTrieNode:
    def __init__(self,handler=None):
        self.children = {}
        self.handler = handler
    #O(n) = 1
    def insert(self, path):
        if path not in self.children:
            self.children[path] = RouteTrieNode()

class RouteTrie:
    def __init__(self):
        self.root = RouteTrieNode()
    
    #O(n) = n, n is the subpaths in the given route
    def insert(self, route, handler):
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

    #O(n) = logn
    def find(self, path):
        splitpaths = path.split("/")
        current_node =self.root
        for p in splitpaths:
            if p!='':
                if p not in current_node.children:
                    return self.find("/404")
                current_node = current_node.children[p]
        if current_node.handler ==None:
            return self.find("/404")

        return current_node.handler


class Router:
    def __init__(self, rooth, nfh):
        self.routetrie = RouteTrie()
        self.routetrie.insert("/",rooth)
        self.routetrie.insert("404",nfh)

    #O(n) = n, n is the subpaths in the given route
    def add_handler(self, path, handler):
        self.routetrie.insert(path,handler)
    
    #O(n) = logn
    def lookup(self, path):
        return self.routetrie.find(path)
                
router = Router("Root handler","not found handler")
router.add_handler("/home/about","Handler about")
router.add_handler("/","root Handler")
router.add_handler("/me","me handler")
print(router.lookup("/")) 
print(router.lookup("/home")) 
print(router.lookup("/home/about")) 
print(router.lookup("/home/about/")) 
print(router.lookup("/home/about/me")) 
