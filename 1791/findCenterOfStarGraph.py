class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        seenNodes = {}

        for edge in edges:
            for point in edge:
                if point in seenNodes:
                    return point
                else:
                    seenNodes[point] = True
        