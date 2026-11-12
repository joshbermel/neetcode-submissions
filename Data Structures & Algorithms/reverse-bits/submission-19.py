class Solution:
    def reverseBits(self, n: int) -> int:
        # during the loop we not only append the first bit to the end 
        # of a new array, but we take 2^i if n != 0


        # we need to first binarize the input, then reverse it
        # every time we can divide by 2, 

        num = n
        sum = 0
        binary = []

        while num != 0:
            # if there is a remainder
            if (num % 2) == 1:
                binary.insert(0,1)

            else:
                binary.insert(0,0)
            num = num // 2   

        # now fill the rest of binary up with as many 0s as need
        diff = 32 - len(binary) - 1
        while diff >= 0:
            binary.insert(0,0)
            diff -= 1 

        for i in range(len(binary)):
            if binary[i] == 1:
                sum += 2**i


        return sum