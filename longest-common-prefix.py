def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        if len(strs) < 1:
            return prefix

        base = min(strs)

        print(base)
        for i in range(len(base)):
            prefix += base[i]
            for s in strs:
                if s[:i+1] != prefix:
                    prefix = prefix[:-1]
                    return prefix
        return prefix
