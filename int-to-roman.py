def intToRoman(num):
        """
        :type num: int
        :rtype: str
        """
        roman = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }

        result = ''

        for k in sorted(roman.keys(), reverse=True):
            count, num = divmod(num, k)
            result += count * roman[k]

        return result
