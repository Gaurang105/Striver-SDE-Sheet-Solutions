class Solution:
    def check(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        prev = None
        rotated_position = None

        for i,num in enumerate(nums):
            if prev!=None and num < prev:
                rotated_position = i
                break
            prev = num

        if not rotated_position:
            return True
            
        return (nums[rotated_position:] + nums[:rotated_position]) == sorted_nums