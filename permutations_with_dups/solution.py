def permutations(w_count, w_left):
    solutions = []

    # No words left
    if w_left == 0:
        return [""]

    for w in w_count:
        if w_count[w] > 0:
            w_count_sub = w_count.copy()
            w_count_sub[w] -= 1

            prefix = w
            suffixes = permutations(w_count_sub, w_left-1)

            solutions.extend([prefix + suffix for suffix in suffixes])

    return solutions

if __name__ == "__main__":
    word = "SALA"

    w_count = {}
    for w in word:
        w_count[w] = w_count.get(w, 0) + 1
    
    perms = permutations(w_count, len(word))

    print(f'Word length: {len(word)}')
    print("Permutations: ", perms)
    print("# Permutations: " + str(len(perms)))