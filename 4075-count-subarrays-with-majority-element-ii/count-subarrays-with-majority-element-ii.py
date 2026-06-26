class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        
        # Step 1: Compute prefix sums of the transformed array (+1 / -1)
        pref = [0] * (n + 1)
        for i in range(n):
            val = 1 if nums[i] == target else -1
            pref[i + 1] = pref[i] + val
            
        # Step 2: Coordinate compression for Fenwick Tree indices
        # Map unique prefix sum values to ranked ranks (1, 2, 3...)
        unique_vals = sorted(list(set(pref)))
        ranks = {val: i + 1 for i, val in enumerate(unique_vals)}
        
        # Step 3: Fenwick Tree (Binary Indexed Tree) operations
        tree_size = len(unique_vals)
        bit = [0] * (tree_size + 1)
        
        def update(idx, delta):
            while idx <= tree_size:
                bit[idx] += delta
                idx += idx & (-idx)
                
        def query(idx):
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & (-idx)
            return s
            
        # Step 4: Count valid pairs P[i] < P[j] with i < j
        ans = 0
        for p_val in pref:
            rank = ranks[p_val]
            # Count how many previous prefix sums have a rank strictly less than current
            ans += query(rank - 1)
            # Insert current prefix sum rank into the Fenwick Tree
            update(rank, 1)
            
        return ans
        