
def get_accum(x):
    y = [0] * (len(x) + 1)

    for i in range(len(x)):
        y[i+1] = y[i] + x[i]

    return y

def max_average_subarray(x, k):
    accum = get_accum(x)
    max = None

    if k >= len(x):
        return (accum[-1] - accum[0]) / len(x)

    for i in range(len(x) - k + 1):
        if max is None or accum[i+k] - accum[i] > max:
            max = accum[i+k] - accum[i]
    return max / k

if __name__ == "__main__":
    print(max_average_subarray([1,12,-5,-6,50,3], 4))