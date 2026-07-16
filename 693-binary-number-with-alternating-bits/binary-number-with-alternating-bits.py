class Solution(object):
    def hasAlternatingBits(self, n):
        prev = n & 1
        n >>= 1
        
        while n > 0:
            curr = n & 1
            if curr == prev:
                return False
            prev = curr
            n >>= 1
            
        return True