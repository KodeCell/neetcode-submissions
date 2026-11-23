class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = {}
        for i, num in enumerate(nums):
            rem = target - num
            if rem in x:
                return[x[rem], i]
            else:
                x[num] = i       