from collections import Counter
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len=0
        freq=Counter(nums)
        for num in freq:
            if num+1 in freq:
                max_len=max(max_len,freq[num]+freq[num+1])
        return max_len


        
