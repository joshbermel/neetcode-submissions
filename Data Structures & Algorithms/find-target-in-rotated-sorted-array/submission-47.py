class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1
        n = len(nums) // 2

        while (l != n):
            # if the left side is sorted
            if (nums[l] < nums[n]):
                # if the target is within the left side
                if (nums[l] <= target <= nums[n]):
                    # shrink window to left
                    r = n
                else:
                    # target is either in the right side or not in nums
                    l = n

            else:
                # if the target is within the right side
                if (nums[n] <= target <= nums[r]):
                    # shrink window to the right
                    l = n
                else:
                    # target is either on the left side or not in nums
                    r = n

            n = (l + r) // 2

        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r
        else:
            return -1
