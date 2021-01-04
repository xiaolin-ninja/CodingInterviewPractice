    def isMatch(s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s

        match = s and p[0] in [s[0],'.']

        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s,p[2:]) or ( match and self.isMatch(s[1:],p))
        else:
            return match and self.isMatch(s[1:],p[1:])
