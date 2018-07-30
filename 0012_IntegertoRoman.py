class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        symbol = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        ans = ''
        for i in range(13):
            ans += symbol[i] * (num // value[i])
            num %= value[i]
        return ans