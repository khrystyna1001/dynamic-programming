# Memoization
def bestSum(targetSum, numbers=[], memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None
    
    shortest = None

    for num in numbers:
        remainder = targetSum - num
        remainder_combination = bestSum(remainder, numbers, memo)
        if remainder_combination != None:
            remainder_combination.append(num)
            combination = remainder_combination
            if (shortest == None or len(combination) < len(shortest)):
                shortest = combination

    memo[targetSum] = shortest
    return shortest

# Tabulation
def best_sum_tabulation(target, numbers=[]):
    table = [None] * (target + 1)
    table[0] = []

    for i in range(target):
        if table[i] is not None:
            for num in numbers:
                if i + num <= target:
                    combination = [*table[i], num]
                    if table[i+num] is None or len(table[i + num]) > len(combination):
                        table[i+num] = combination
    return table[target]

if __name__ == "__main__":
    # print(bestSum(7, [5,3,4,7]))
    # print(bestSum(8, [2,3,5]))
    print(best_sum_tabulation(7, [5,3,4,7]))
    print(best_sum_tabulation(8, [2,3,5]))