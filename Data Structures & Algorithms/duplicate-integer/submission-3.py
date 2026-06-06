class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # naive solution: for each value, check the rest of the array
        # for that value, if it exists, return false, otw return true
        # this is n^2 time complexity tho

        # hash solution: create a hashmap as you comb through each value
        # before adding, check for existence. If already in, return false
        # if not, add and move forward

        s = set()

        for num in nums:
            if num in s:
                return True
            s.add(num)

        return False