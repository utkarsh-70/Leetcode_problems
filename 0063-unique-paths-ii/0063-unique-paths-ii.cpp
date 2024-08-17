class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int n = obstacleGrid.size();
        int m = obstacleGrid[0].size();
        
        if (obstacleGrid[n-1][m-1] == 1 || obstacleGrid[0][0] == 1) {
            return 0;
        }

        vector<vector<long long>> dp(n, vector<long long>(m, 0));
    
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (obstacleGrid[i][j] == 1) {
                    dp[i][j] = -1;
                }
            }
        }
        
        dp[n-1][m-1] = 1;

        for (int i = n - 1; i >= 0; i--) {
            for (int j = m - 1; j >= 0; j--) {
                if (dp[i][j] == -1) {
                    dp[i][j] = 0;
                    continue;
                }
                if (i != n - 1) {
                    dp[i][j] += dp[i + 1][j];
                }
                if (j != m - 1) {
                    dp[i][j] += dp[i][j + 1];
                }
            }
        }

        return dp[0][0];
    }
};
