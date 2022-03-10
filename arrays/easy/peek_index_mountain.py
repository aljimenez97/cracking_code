# https://leetcode.com/problems/peak-index-in-a-mountain-array/

# Given an integer array arr that is guaranteed to be a mountain, return any i such 
# that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

def find_peek(array):
    for i in range(1, len(array) - 1):
        if (array[i] - array[i-1]) > 0 and (array[i] - array[i+1]) > 0:
            return i

if __name__ == "__main__":
    arr = [0,2,1,0]
    print(find_peek(arr))
