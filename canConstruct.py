def can_construct (target, word_bank=[], memo={}):
    if target in memo:
        return memo[target]
    if target == '':
        return True
    for word in word_bank:
        if word_bank.index(word) == 0:
            suffix = target[len(word)::]
            if can_construct(suffix, word_bank, memo) == True:
                memo[target] = True
                return True
    memo[target] = False
    return False
    
if __name__ == "__main__":
    print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))