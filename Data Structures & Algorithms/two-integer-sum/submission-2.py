class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for n in range(len(nums)): 
            h[nums[n]] = n
        
        for n in range(len(nums)): 
            num = target - nums[n]
            if num in h and h[num] != n:
                return [n, h[num]]