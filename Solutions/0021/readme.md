![results](image.png)

Sorting is a dangerous operation, as it can easily evolve into a O(N^2) operation. The goal is to sort in anything less than that. Fortunately, most of the work has already been done for us, we just need to combine the lists efficiently.To do this, I iterated over the lists recursively. I assigned the next largest value to be the next value until I reached the end of the list. When I reached the end of the list, I returned nonempty list. This will only touch each node once, making it a much more appealing O(N + M).
