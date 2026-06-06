class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create a dictionary of each word. The characters will be the 
        # keys and the frequency will be the values. Ensure that each
        # key value pair matches. 

        if len(s) != len(t):
            return False

        s_dict = dict()
        t_dict = dict()        
        
        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1

        for char in t:
            if char in t_dict:
                t_dict[char] += 1
            else:
                t_dict[char] = 1

        for key in s_dict:
            if key not in t_dict or s_dict[key] != t_dict[key]:
                return False

        return True