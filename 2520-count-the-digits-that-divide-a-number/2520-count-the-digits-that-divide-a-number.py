class Solution(object):
    def countDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        curr = num

        while curr > 0:
            digit = curr % 10
            if num % digit == 0:
                count += 1
            curr //= 10

        return count