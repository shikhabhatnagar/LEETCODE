import fractions

class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        prefixGcd = []
        current_max = 0
        
        for num in nums:
            current_max = max(current_max, num)
            # Use fractions.gcd for Python 2
            prefixGcd.append(fractions.gcd(num, current_max))
            
        prefixGcd.sort()
        
        total_sum = 0
        left = 0
        right = n - 1
        
        while left < right:
            total_sum += fractions.gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
            
        return total_sum