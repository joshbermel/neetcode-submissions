class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        d = dict()
        ans = []

        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        sorted_keys = sorted(d, key=d.get, reverse=True)
        return sorted_keys[:k]
        
        # while k > 0:
        #     # append the key with the highest value to ans
        #     highest_key = max(d, key=d.get)
        #     ans.append(highest_key)
        #     # remove that key-value pair from d
        #     del d[highest_key]
        #     # reduce k by 1
        #     k -= 1
        
        # return ans
