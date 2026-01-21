def count_construct(target, word_bank=[]):
    if target == '':
        return 1
    total_count = 0
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            num_ways_for_rest = count_construct(suffix, word_bank)
            total_count += num_ways_for_rest
    return total_count

if __name__ == "__main__":
    print(count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))