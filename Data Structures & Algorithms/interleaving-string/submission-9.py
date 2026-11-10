class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        n, m = len(s1), len(s2)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for j in range(n + 1):
            for k in range(m + 1):
                if j == 0 and k == 0:
                    continue
                from_s1 = j > 0 and dp[j - 1][k] and s1[j - 1] == s3[j + k - 1]
                from_s2 = k > 0 and dp[j][k - 1] and s2[k - 1] == s3[j + k - 1]
                dp[j][k] = from_s1 or from_s2

        return dp[n][m]