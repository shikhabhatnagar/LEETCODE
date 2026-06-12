class SegmentTree:
    def __init__(self, sorted_x):
        self.sorted_x = sorted_x
        self.n = len(sorted_x) - 1
        # Allocate size for the tree arrays
        size = 1 << ((self.n - 1).bit_length() + 1)
        self.tree = [0] * size  # Stores total unique width covered in the node's interval
        self.cnt = [0] * size   # Tracks how many active squares fully cover this interval

    def update(self, ql, qr, val, l, r, i):
        # Query interval completely outside current node segment
        if ql >= r or qr <= l:
            return
        
        # Query interval completely covers current node segment
        if ql <= l and r <= qr:
            self.cnt[i] += val
        else:
            mid = l + (r - l) // 2
            self.update(ql, qr, val, l, mid, 2 * i)
            self.update(ql, qr, val, mid, r, 2 * i + 1)
        
        # Push up logic: Update unique width for segment `i`
        if self.cnt[i] > 0:
            self.tree[i] = self.sorted_x[r] - self.sorted_x[l]
        else:
            if r - l == 1:
                self.tree[i] = 0
            else:
                self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]


class Solution(object):
    def separateSquares(self, squares):
        """
        :type squares: List[List[int]]
        :rtype: float
        """
        events = []
        x_coords = set()
        
        # Process every square into entry and exit events
        for x, y, l in squares:
            events.append((y, 1, x, x + l))       # Bottom edge: adds a square
            events.append((y + l, -1, x, x + l))  # Top edge: removes a square
            x_coords.add(x)
            x_coords.add(x + l)
            
        # Sort events primarily by y-coordinate
        events.sort(key=lambda e: e[0])
        
        # Coordinate compression for X coordinates
        sorted_x = sorted(x_coords)
        x_to_idx = {x: i for i, x in enumerate(sorted_x)}
        
        # Initialize segment tree
        st = SegmentTree(sorted_x)
        
        # Pass 1: Calculate the total union area
        prev_y = events[0][0]
        intervals = []
        
        for y, val, x1, x2 in events:
            if y != prev_y:
                # Store the strip details: (start_y, end_y, active_width)
                intervals.append([prev_y, y, st.tree[1]])
                prev_y = y
            st.update(x_to_idx[x1], x_to_idx[x2], val, 0, len(sorted_x) - 1, 1)
            
        total_area = sum((y2 - y1) * width for y1, y2, width in intervals)
        target_half_area = total_area / 2.0
        
        # Pass 2: Accumulate area until we hit the target half mark
        accumulated_area = 0.0
        for y1, y2, width in intervals:
            strip_area = (y2 - y1) * width
            if accumulated_area + strip_area >= target_half_area:
                # The dividing line lies strictly within this y-interval
                remaining_needed = target_half_area - accumulated_area
                return y1 + (remaining_needed / width)
            accumulated_area += strip_area
            
        return 0.0
        