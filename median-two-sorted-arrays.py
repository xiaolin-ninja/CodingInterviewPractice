    def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums3 = (nums1 + nums2).sort()
        length = len(nums3)
        mid = length / 2

        if length % 2 == 0:
            return (nums3[mid] + nums3[mid-1]) / 2.0
        return nums3[mid]
