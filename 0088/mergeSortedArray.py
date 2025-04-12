class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if nums2 == []:
            return
        elif nums1 == []:
            return

        if set(nums1) == {0}:
            nums1[m:] = nums2
            return

        for i in range(0, n):
            nums1.pop()

        nums1.extend(nums2)
        nums1.sort()

    def quick_sort(list):
        if len(list) == 1:
            return list    

        