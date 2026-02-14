class Solution:
   
 def champagneTower(self,poured, query_row, query_glass):
    dp = [[0]*(k+1) for k in range(query_row+1)]
    dp[0][0] = poured
    
    for r in range(query_row):
        for c in range(len(dp[r])):
            overflow = (dp[r][c] - 1) / 2
            if overflow > 0:
                dp[r+1][c] += overflow
                dp[r+1][c+1] += overflow
    
    return min(1, dp[query_row][query_glass])
