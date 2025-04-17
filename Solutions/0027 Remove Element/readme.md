# [Remove Element](https://leetcode.com/problems/remove-element/)

![results](image.png)

For this problem, I wanted to removed target elements without deleting them in place, because if I just removed them then we would need to shift all of the other elements over, which can get burdensome on a machine. I found a solution by realizing that the order of the values returned does not matter. Because of that, I can reliably replace the value with the last element of the array. This is a O(1) operation. I then just delete the last element (once again, an O(1) operation) to ensure that I do not deal with duplicates.
