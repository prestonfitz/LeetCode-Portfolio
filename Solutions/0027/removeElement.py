class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        inc = 0
        
        while inc < len(nums):
            if nums[inc] == val:
                nums[inc] = nums[-1]
                del nums[inc]
            else:
                inc += 1

        return (len(nums))
        