class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        nums[:n] = reversed(nums[:n])
        nums[k:n] = reversed(nums[k:n])
        nums[:k] = reversed(nums[:k])