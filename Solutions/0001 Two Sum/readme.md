# [Two Sum](https://leetcode.com/problems/two-sum/description/)

![results](image.png)

I wanted, if at all possible, to avoid comparing each number against another, as this would result in an O(N^2) time complexity solution, which is no good. As I thought of how to do this, I actually took some inspiration from memoization. Why redo a calculation if it has already been done? So, rather than adding numbers together, I subtracted the number from the target and compared the result (compliment) to a dictionary. If the result was a key in the dictionary, then I would return the related value and pass that value and the index of the other number. If not, I would store the number as a key and its index as a value. This means that I only have to iterate through the array once, which brings the problem down to O(N).
