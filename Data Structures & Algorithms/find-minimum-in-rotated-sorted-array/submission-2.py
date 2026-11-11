class Solution:
    def findMin(self, nums: List[int]) -> int:

        # split array in 2 and looks for the side where the left is higher than
        # the right

        n = len(nums) // 2
        l = 0
        r = len(nums) - 1

        while (l != n):
            # if in order, return far left (min)
            if (nums[l] <= nums[n]) and (nums[n] <= nums[r]):
                return nums[l]
            # if min is on left
            elif (nums[l] > nums[n]):
                r = n
            # min is on right
            else:
                l = n
            
            n = (r + l) // 2
        
        return nums[r]

