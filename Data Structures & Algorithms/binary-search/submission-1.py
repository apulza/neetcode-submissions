class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Found the target, return its index
            if nums[mid] == target:
                return mid
            # Target is larger, discard the left half
            elif nums[mid] < target:
                left = mid + 1
            # Target is smaller, discard the right half
            else:
                right = mid - 1
                
        # Target not found in the array
        return -1