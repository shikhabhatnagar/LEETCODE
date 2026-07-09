class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[bool]
        """
        # Array to store the component ID for each node
        component = [0] * n
        curr_id = 0
        
        # Linear scan to group nodes into continuous connected segments
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                curr_id += 1
            component[i] = curr_id
            
        # Answer each query in O(1) time
        ans = []
        for u, v in queries:
            ans.append(component[u] == component[v])
            
        return ans