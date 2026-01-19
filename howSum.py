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


if __name__ == "__main__":
    print(howSum(7, [2,3,4,5]))
    print(howSum(7, [5,3,4,7]))