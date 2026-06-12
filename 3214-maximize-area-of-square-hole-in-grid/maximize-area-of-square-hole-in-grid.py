class Solution(object):
    def maximizeSquareHoleArea(self, n, m, hBars, vBars):
        """
        :type n: int
        :type m: int
        :type hBars: List[int]
        :type vBars: List[int]
        :rtype: int
        """
        def getMaxConsecutive(bars):
            bars.sort()
            max_consective = 1
            current_streak = 1
            
            for i in range(1, len(bars)):
                if bars[i] == bars[i-1] + 1:
                    current_streak += 1
                else:
                    max_consective = max(max_consective, current_streak)
                    current_streak = 1
                    
            return max(max_consective, current_streak)
        
        # Find the maximum consecutive bars we can remove
        max_h_bars = getMaxConsecutive(hBars)
        max_v_bars = getMaxConsecutive(vBars)
        
        # The maximum side length of a gap is (number of consecutive bars removed + 1)
        max_side = min(max_h_bars + 1, max_v_bars + 1)
        
        return max_side * max_side

        
        