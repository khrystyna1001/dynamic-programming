# Memoization
def all_construct(target, word_bank=[], memo={}):
    if target in memo:
        return memo[target]
    if target == '':
        return [[]]
    result = []
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, word_bank, memo)
            target_ways = [[word, *way] for way in suffix_ways]
            result.extend(target_ways)
    memo[target] = result
    return result

# Tabulation
def all_construct_tabulation(target, word_bank=[]):
    table = [[] for _ in range(len(target) + 1)]
    table[0] = [[]]
    for i in range(len(target)):
        for word in word_bank:
            if target[i:i + len(word)] == word:
                new_combinations = [sub_array + [word] for sub_array in table[i]]
                if i + len(word) <= len(target):
                    table[i + len(word)].extend(new_combinations)
    return table[len(target)]

if __name__ == "__main__":
    # print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
    print(all_construct_tabulation('purple', ['purp', 'p', 'ur', 'le', 'purpl']))