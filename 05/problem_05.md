# Autocomplete with tries

- TrieNode
    - Insert 
        - Time: O(n) = n
        - Space: O(n) = n [n -> chars in word]
    - suffixes
        - Time:O(n) = logn - nlogn [ Due to recursion for specific tree and subchilgd]
        - Space: O(n) = n [n-> return autocomplete list of values]
- Trie
    - insert
        - Time: O(n) = n*m,  n- no of chars, m-no of children
        - Space: O(n) = n [n-> chars in word]
    - find:
        - Time: O(n) = n*m,  n- no of chars, m-no of children
        - Space: O(n) = 1

Note:
-Considering Averge case for "element in dict" = O(n) = 1
References
https://wiki.python.org/moin/TimeComplexity