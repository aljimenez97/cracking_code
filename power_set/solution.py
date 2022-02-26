# Write a method to return all subsets of a set

sample_set = {1,2,3,4,5,6,7,8,9}


def get_subsets(my_set):
    all_subsets = [set()]

    for n in my_set:
        for subet in list(all_subsets):
            all_subsets.append(subet.union({n}))

    return len(all_subsets)


if __name__ == "__main__":
    print(get_subsets(sample_set))