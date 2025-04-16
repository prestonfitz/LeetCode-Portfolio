![results](image.png)

Linked lists are interesting in that they can loop back in themselves, because they are just connected by pointers. As such, it is important to know know if we have seen a particular node before. Fortunately, in python, we can hash an entire object. Thus, I can add each node to a dictionary and then quickly see if that node exists already in the dictionary. By using the node rather than the value, we allow the potential for multiple nodes to have the same value without counting them as a loop.
