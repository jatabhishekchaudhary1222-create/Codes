class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        write = 1  # position to write the next unique element
        for read in range(1, len(nums)):
            if nums[read] != nums[read - 1]:  # new unique value
                nums[write] = nums[read]
                write += 1
        return write
