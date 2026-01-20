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

if __name__ == "__main__":
    print(bestSum(7, [5,3,4,7]))
    print(bestSum(8, [2,3,5]))