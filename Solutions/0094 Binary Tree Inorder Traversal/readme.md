# [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)

![results](image.png)

This problem lends itself well to recursion. We start by moving as far left as we can. The base case is when we have hit an empty node. We then move up a level and attach whatever nodes we have stacked up to a list. We then attach the current node and then its right children. Those nodes are passed up and concatenated until we have covered the entire tree.
