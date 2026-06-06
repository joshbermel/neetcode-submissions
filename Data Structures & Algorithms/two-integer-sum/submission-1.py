class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        i = 0
        n = len(nums)
        found = False;
        while i < (n - 1):
            j = i + 1
            while j < n:
                if (nums[i] + nums[j]) == target:
                    ans.append(i)
                    ans.append(j)
                    found = True
                    break
                else:
                    j += 1
            if found:
                break
            i += 1
        return ans