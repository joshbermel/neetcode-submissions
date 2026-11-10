class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:        
        ans = []
        nums.sort()

        # i can go up to the third last element
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j != k:
                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum < 0:
                    j += 1
                elif curr_sum > 0:
                    k -= 1
                    continue
                else:
                    sol = [nums[i], nums[j], nums[k]]
                    if sol not in ans:
                        ans.append(sol)
                    k -= 1

        return ans
