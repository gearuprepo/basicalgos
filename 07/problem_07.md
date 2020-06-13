# Request routing using Trie

- RouteTrieNode
    - insert 
        - Time O(n) : n, n-> no of child nodes
        - Space O(n) : n [based on the path]
- RouteTrie
    - insert
        - Time: #O(n) = n*m, n is the subpaths in the given route, m us the sub elements in tree
        - Space O(n) = n
    - find
        - Time O(n) = n*m, n- paths, m - children nodes    
        - Space O(n)= n
- Router
    - add_handler
        - Time: #O(n) = n*m, n is the subpaths in the given route, m us the sub elements in tree
        - Space O(n) = n
    - lookup
        - Time O(n) = n*m, n- paths, m - children nodes    
        - Space O(n)= n

Note:
-Considering Averge case for "element in dict" = O(n) = 1
References
https://wiki.python.org/moin/TimeComplexity