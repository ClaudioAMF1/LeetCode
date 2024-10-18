class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num
        
        @functools.cache
        def dfs(index, current_or):
            if index == len(nums):
                return 1 if current_or == max_or else 0
            
            count_with = dfs(index + 1, current_or | nums[index])
            count_without = dfs(index + 1, current_or)
            
            return count_with + count_without
        
        return dfs(0, 0)
