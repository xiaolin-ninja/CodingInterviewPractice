def threeSum(nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        length, results = len(nums), []

        nums.sort()

        for i in range(length - 2):
            j, k = i+1, length - 1

            while j < k:
                triplet = [nums[i], nums[j], nums[k]]
                _sum = sum(triplet)

                if _sum == 0 and triplet not in results:
                    results.append(triplet)
                    j += 1
                    k -= 1

                elif _sum < 0:
                    j += 1

                else:
                    k -= 1

        return results
