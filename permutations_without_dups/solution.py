def permutations(word, prefix = "", dyn = {}):
    if word in dyn:
        return dyn[word]

    if word == "":
        return ""
    elif len(word) == 1:
        return [prefix + word] 
    else:
        solutions = []

        for w in word:
            partial_perms = permutations(word.replace(w, ""), prefix + w, dyn)
            solutions.extend(partial_perms)
        dyn[word] = solutions
    return dyn[word]

if __name__ == "__main__":
    word = "PILOT"
    perms = permutations(word, "", {})

    print(f'Word length: {len(word)}')
    print("Permutations: ", perms)