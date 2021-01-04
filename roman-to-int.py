def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        roman = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }

        n = roman[s[0]]

        for i in range(1, len(s)):
            curr = roman[s[i]]
            prev = roman[s[i-1]]

            if curr > prev:
                n -= 2*prev
            n += curr

        return n

