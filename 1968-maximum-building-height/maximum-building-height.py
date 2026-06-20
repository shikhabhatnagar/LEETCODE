class Solution(object):
    def maxBuilding(self, n, restrictions):
        """
        :type n: int
        :type restrictions: List[List[int]]
        :rtype: int
        """
        # Add the boundary restrictions
        restrictions.append([1, 0])
        restrictions.append([n, n - 1])
        
        # Sort by building ID
        restrictions.sort()
        
        m = len(restrictions)
        
        # Left-to-Right Pass: Propagate limits forward
        for i in range(1, m):
            id1, h1 = restrictions[i - 1]
            id2, h2 = restrictions[i]
            restrictions[i][1] = min(h2, h1 + (id2 - id1))
            
        # Right-to-Left Pass: Propagate limits backward
        for i in range(m - 2, -1, -1):
            id1, h1 = restrictions[i]
            id2, h2 = restrictions[i + 1]
            restrictions[i][1] = min(h1, h2 + (id2 - id1))
            
        # Calculate the absolute maximum height between any two adjacent restricted buildings
        max_ans = 0
        for i in range(1, m):
            id1, h1 = restrictions[i - 1]
            id2, h2 = restrictions[i]
            
            # The peak formula between two bounds
            peak = (h1 + h2 + (id2 - id1)) // 2
            max_ans = max(max_ans, peak)
            
        return max_ans
        