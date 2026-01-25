# memoization
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

def can_construct_tabulation(target, word_bank=[]):
    table = [False] * (len(target) + 1)
    table[0] = True

    for i in range(len(target)):
        if table[i]:
            for word in word_bank:
                if target[i:i + len(word)] == word:
                    table[i + len(word)] = True
    return table[len(target)]
    
if __name__ == "__main__":
    # print(can_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
    print(can_construct_tabulation("abcdef", ["ab", "abc", "cd", "def", "abcd"]))