class Solution(object):
    def romanToInt(self, s):
        value = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "C" : 100,
            "L" : 50,
            "D" : 500,
            "M" : 1000 
        }

        ans = 0
        for i in range(len(s)):
            if i < len(s) - 1 and value[s[i]] < value[s[i + 1]]:
                ans -= value[s[i]]
            else:
                ans += value[s[i]]

        return ans
        