# Request routing using Trie

- RouteTrieNode
    - insert 
        - Time O(n) :1
        - Space O(n) : n [based on the path]
- RouteTrie
    - insert
        - Time/Space: #O(n) = n, n is the subpaths in the given route
    - find
        - Time O(n) = n, n is the subpaths in the given route
        - Space O(n)= n
- Router
    - add_handler
        - Time/Space: #O(n) = n, n is the subpaths in the given route
    - lookup
        - Time O(n) = n
        - Space O(n)= n

Note:
-Considering Averge case for "element in dict" = O(n) = 1
References
https://wiki.python.org/moin/TimeComplexity