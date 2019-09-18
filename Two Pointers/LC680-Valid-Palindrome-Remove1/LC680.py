class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # characters are all letters, do not need to check alnum
        if not s:
            return True

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # delete left / right
                # only need to check string between left and right: s[left:right+1]
                return self.isPalindrome(s[left + 1:right + 1]) or self.isPalindrome(s[left:right])

            left += 1
            right -= 1

        return True

    def isPalindrome(self, s):
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

        # T:O(n)  S:O(1)
