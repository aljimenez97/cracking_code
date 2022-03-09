

def get_accum(x):
    y = [0] * (len(x) + 1)

    for i, x in enumerate(x):
        y[i+1] = y[i] + x
    
    return y

def fair_index(A, B):
    count = 0

    accum_a = get_accum(A)
    accum_a_rev = get_accum(A[::-1])[::-1]

    accum_b = get_accum(B)
    accum_b_rev = get_accum(B[::-1])[::-1]

    print(accum_a)
    print(accum_a_rev)
    print(accum_b)
    print(accum_b_rev)

    for i in range(1, len(accum_a) - 1):
        if accum_a[i] == accum_a_rev[i] == accum_b[i] == accum_b_rev[i]:
            count += 1

    return count

if __name__ == "__main__":
    A = [2, -2, -3, 3]
    B = [0, 0, 4, -4]

    print(fair_index(A, B))