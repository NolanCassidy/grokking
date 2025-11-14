# https://leetcode.com/problems/single-element-in-a-sorted-array/

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # We will use binary search on indices, not on values directly.
        left, right = 0, len(nums) - 1
        
        # Loop until the search space collapses to one element
        while left < right:
            # Standard binary search mid
            mid = (left + right) // 2
            
            # Ensure mid is even so that mid and mid + 1 form a "pair position"
            if mid % 2 == 1:
                mid -= 1  # make it even
            
            # Now mid is even. Compare the pair (mid, mid + 1).
            if nums[mid] == nums[mid + 1]:
                # Case 1: This pair is valid (like [x,x])
                # That means everything up to mid+1 is "normal" pairs,
                # so the single element must be to the RIGHT of mid+1.
                left = mid + 2
            else:
                # Case 2: This pair is broken.
                # That means the single element is either at mid
                # or somewhere to the LEFT of mid.
                right = mid
        
        # When left == right, we've narrowed it down to the single element.
        return nums[left]
