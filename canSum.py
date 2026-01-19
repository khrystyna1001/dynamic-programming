def canSum(targetSum, numbers=[]):
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    for num in numbers:
        rem = targetSum - num
        if (canSum(rem, numbers) == True):
            return True
        
    return False


if __name__ == "__main__":
    print(canSum(7, [2,3,4,5]))
