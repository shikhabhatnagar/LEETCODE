import sys
# Increase recursion depth for deep trees during DFS
sys.setrecursionlimit(200000)

class Solution(object):
    def assignEdgeWeights(self, edges, queries):
        """
        :type edges: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges) + 1
        MOD = 10**9 + 7
        
        # Step 1: Build Adjacency List
        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        # Binary Lifting Setup
        # LOG is enough to cover n <= 10^5 (2^17 = 131072)
        LOG = 18 
        up = [[0] * LOG for _ in range(n + 1)]
        depth = [0] * (n + 1)
        
        # Step 2: DFS to populate depths and immediate parents (up[node][0])
        def dfs(node, parent, d):
            depth[node] = d
            up[node][0] = parent
            for neighbor in adj[node]:
                if neighbor != parent:
                    dfs(neighbor, node, d + 1)
                    
        dfs(1, 1, 0)
        
        # Step 3: Compute the binary lifting table
        for j in range(1, LOG):
            for i in range(1, n + 1):
                up[i][j] = up[up[i][j-1]][j-1]
                
        # Helper function to find LCA using Binary Lifting
        def get_lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
                
            # Bring both nodes to the same depth
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = up[u][j]
                    
            if u == v:
                return u
                
            # Lift both nodes simultaneously right below their LCA
            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
                    
            return up[u][0]

        # Step 4: Process all queries
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            lca = get_lca(u, v)
            # Total edges on the path between u and v
            k = depth[u] + depth[v] - 2 * depth[lca]
            
            # Answer is 2^(k - 1) % MOD
            ans.append(pow(2, k - 1, MOD))
            
        return ans