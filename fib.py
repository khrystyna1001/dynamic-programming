# Memoization
def fib(n, memo = {}):
    if (n in memo):
        return memo[n]
    
    if (n <= 2):
        return 1
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]

# Tabulation
def fib_tabulation(n):
    table = [0] * (n+3)
    table[1] = 1
    for i in range(n):
        table[i+1] += table[i]
        table[i+2] += table[i]

    return table[n]

if __name__ == "__main__":
    # print(fib(50))
    print(fib_tabulation(6))