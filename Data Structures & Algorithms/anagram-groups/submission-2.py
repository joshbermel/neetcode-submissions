class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # go through each string in the array
        # sort the letters in each string and use that as a key
        # if the key exists in the dict, add the original word

        d = dict()

        for word in strs:
            key = ''.join(sorted(word))
            if key in d:
                d[key].append(word)
            else:
                d[key] = [word]

        return list(d.values())
