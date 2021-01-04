def maxArea(height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        l = 0
        r = len(height)-1

        while l < r:
            w = r - l
            left = height[l]
            right = height[r]

            max_area = max(max_area, min(left, right) * w)
            if left < right:
                l += 1
            else:
                r -=1

        return max_area
