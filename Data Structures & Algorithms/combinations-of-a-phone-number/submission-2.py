class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # size of output is 3^n where n is the num of digits

        # digits length will only ever be 4 or less

        d = {}
        output = []
    


        d['2'] = ["a", "b", "c"]
        d['3'] = ["d", "e", "f"]
        d['4'] = ["g", "h", "i"]
        d['5'] = ["j", "k", "l"]
        d['6'] = ["m", "n", "o"]
        d['7'] = ["p", "q", "r", "s"]
        d['8'] = ["t", "u", "v"]
        d['9'] = ["w", "x", "y", "z"]

        if len(digits) == 0:
            return []

        new_output = d[digits[0]]

        for i in range(len(digits)):
            if i == 0:
                continue
            new_chars = d[digits[i]]
            output = new_output
            new_output = []
            for char in output:
                for new_char in new_chars:
                    new_output.append(char + new_char)

        return new_output

    