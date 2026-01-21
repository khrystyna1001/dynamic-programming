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

if __name__ == "__main__":
    print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))