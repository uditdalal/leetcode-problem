class Solution(object):
    def numberOfSteps(self, num):
        if num == 0:
            return 0
        return (num.bit_length() - 1) + bin(num).count('1')