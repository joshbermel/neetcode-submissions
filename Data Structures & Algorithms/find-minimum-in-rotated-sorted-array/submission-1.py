class Solution:
    def findMin(self, nums: List[int]) -> int:
        # to find the min we need to know how many times it was rotated modulo n
        # then we access that element in the array

        # 1) extract rotation number, r,  in log n time
        # 2) take modulo n
        # 3) access nums[r] as the min

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

