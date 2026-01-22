# Memoization
def gridTravel (m, n, memo = {}):
    key = str(m) + ',' + str(n)

    if (key in memo):
        return memo[key]
    
    if (m == 1 and n == 1):
        return 1
    
    if (m == 0 or n == 0):
        return 0
    
    memo[key] = gridTravel(m - 1, n, memo) + gridTravel(m, n - 1, memo)
    return memo[key]

# Tabulation
def grid_traveler_tabulation(m, n):
    table = [[0] * (n + 1) for _ in range(m + 1)]
    table[1][1] = 1
    for i in range(m+1):
        for j in range(n+1):
            current = table[i][j]
            if (j+1 <= n):
                table[i][j+1] += current
            if (i+1 <= m):
                table[i+1][j] += current
    return table[m][n]

if __name__ == "__main__":
    #print(gridTravel(18, 18))
    print(grid_traveler_tabulation(3, 3))