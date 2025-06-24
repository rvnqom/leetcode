class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        result=set()
        for j in range(len(nums)):
            if nums[j]==key:
                for i in range(max(0,j-k),min(len(nums),j+k+1)):
                    result.add(i)
        return sorted(result)
        
