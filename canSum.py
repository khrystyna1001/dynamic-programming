# Memoization
def canSum(targetSum, numbers=[], memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    for num in numbers:
        rem = targetSum - num
        if (canSum(rem, numbers, memo) == True):
            memo[targetSum] = True
            return True
        
    memo[targetSum] = False
    return False

# Tabulation
def can_sum_tabulation(target, numbers):
    table = [False]*(target+1)
    table[0] = True
    for i in range(len(table)):
        if (table[i] == True):
            for num in numbers:
                if i+num <= target:
                    table[i+num] = True
    return table[target]

if __name__ == "__main__":
    # print(canSum(7, [2,3,4,5]))
    print(can_sum_tabulation(7, [2,3,4,5]))
