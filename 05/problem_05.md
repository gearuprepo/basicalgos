# Autocomplete with tries

- TrieNode
    - Insert 
        - Time: O(n) = 1
        - Space: O(n) = n [n -> chars in word]
    - suffixes
        - Time:O(n) = logn - nlogn [ Due to recursion for specific tree and subchilg]
        - Space: O(n) = n [n-> return autocomplete list of values]
- Trie
    - insert
        - Time: O(n) = n
        - Space: O(n) = n [n-> chars in word]
    - find:
        - Time: O(n) = n
        - Space: O(n) = 1
