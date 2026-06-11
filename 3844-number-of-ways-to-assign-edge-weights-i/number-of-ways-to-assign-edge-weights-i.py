class Solution(object):
    def assignEdgeWeights(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        
        # Step 1: Build the adjacency list for the tree
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # Step 2: Use BFS to find the maximum depth (distance from root 1)
        max_depth = 0
        queue = [(1, 0)] # (current_node, current_depth)
        visited = {1}
        
        while queue:
            node, depth = queue.pop(0)
            max_depth = max(max_depth, depth)
            
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, depth + 1))
        
        # Step 3: Calculate 2^(max_depth - 1) % (10^9 + 7)
        # Handle the edge case where max_depth is 0 (though constraints say n >= 2, so max_depth >= 1)
        if max_depth == 0:
            return 0
            
        MOD = 10**9 + 7
        return pow(2, max_depth - 1, MOD)
        