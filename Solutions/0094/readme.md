![results](image.png)

This code was heavily influenced by the textbook’s in order traversal function. The difference is that I had to figure out how to store it. Fortunately, that is not too different than just simply printing the values of the tree. We can do this recursively. The base case is when we have hit an empty node. We then move up a level and attach whatever nodes we have stacked up to a list. We then attach the current node and then its right children. Those nodes are passed up and concatenated until we have covered the entire tree.
