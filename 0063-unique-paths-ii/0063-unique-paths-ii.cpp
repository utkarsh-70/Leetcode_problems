class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int n = obstacleGrid.size();
        int m = obstacleGrid[0].size();
        
        // If the start or end cell has an obstacle, return 0
        if (obstacleGrid[n-1][m-1] == 1 || obstacleGrid[0][0] == 1) {
            return 0;
        }

        // Use long long to prevent integer overflow
        vector<vector<long long>> dp(n, vector<long long>(m, 0));
        
        // Initialize the grid, marking obstacles as -1
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (obstacleGrid[i][j] == 1) {
                    dp[i][j] = -1;
                }
            }
        }
        
        // Set the destination cell to 1 if it is not an obstacle
        dp[n-1][m-1] = 1;

        // Fill the DP table by iterating from bottom-right to top-left
        for (int i = n - 1; i >= 0; i--) {
            for (int j = m - 1; j >= 0; j--) {
                // If the cell is an obstacle, set paths to 0
                if (dp[i][j] == -1) {
                    dp[i][j] = 0;
                    continue;
                }
                // Add paths from the cell below (if within bounds)
                if (i != n - 1) {
                    dp[i][j] += dp[i + 1][j];
                }
                // Add paths from the cell to the right (if within bounds)
                if (j != m - 1) {
                    dp[i][j] += dp[i][j + 1];
                }
            }
        }

        // Return the number of unique paths from the start cell
        return dp[0][0];
    }
};
