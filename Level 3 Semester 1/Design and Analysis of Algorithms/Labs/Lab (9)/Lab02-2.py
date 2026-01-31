def lcs_string(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    
    i, j = m, n
    lcs_seq = []

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_seq.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs_seq))



X = "ABCBDAB"
Y = "BDCABA"

print("String X:", X)
print("String Y:", Y)
print("LCS:", lcs_string(X, Y))
print("Length of LCS:", len(lcs_string(X, Y)))
