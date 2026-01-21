def all_construct(target, word_bank):
    if target == '':
        return [[]]
    result = []
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, word_bank)
            target_ways = [[word, *way] for way in suffix_ways]
            result.extend(target_ways)
    return result

if __name__ == "__main__":
    print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))