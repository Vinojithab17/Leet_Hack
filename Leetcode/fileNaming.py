MOD = 10**9 + 7

def renameFile(oldName, newName):
    m, n = len(newName), len(oldName)
    # Create a DP table with (m+1) x (n+1) dimensions
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # If newName is empty, there's one way to form it from any prefix of oldName
    for j in range(n + 1):
        dp[0][j] = 1
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if newName[i - 1] == oldName[j - 1]:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i][j - 1]) % MOD
            else:
                dp[i][j] = dp[i][j - 1]
    
    return dp[m][n]

# Example usage:
oldName = "ababa"
newName = "aba"
print(renameFile(oldName, newName))  # Output: 4
