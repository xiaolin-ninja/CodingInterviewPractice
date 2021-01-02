    def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        substr = ''
        longest = 0

        for c in s:
            if c in substr:
                i = substr.index(c)
                substr = substr[i+1:]
            substr += c
            longest = max(longest, len(substr))
        return longest
