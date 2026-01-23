# Memoization
def howSum(targetSum, numbers=[], memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    for num in numbers:
        remainder = targetSum - num
        remainderResult = howSum(remainder, numbers, memo)
        if (remainderResult is not None):
            remainderResult.append(num)
            memo[targetSum] = remainderResult
            return memo[targetSum]
    memo[targetSum] = None
    return None

# Tabulation
def how_sum_tabulation(target, numbers=[]):
    table = [None] * (target + 1)
    table[0] = []
    for i in range(target):
        if (table[i] != None):
            for num in numbers:
                if i + num <= target:
                    table[i+num] = [*table[i], num]

    return table[target]


if __name__ == "__main__":
    # print(howSum(7, [2,3,4,5]))
    # print(howSum(7, [5,3,4,7]))
    print(how_sum_tabulation(7, [2,3,4,5]))
    print(how_sum_tabulation(7, [5,3,4,7]))