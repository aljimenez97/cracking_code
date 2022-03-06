# https://leetcode.com/problems/container-with-most-water/

# You are given an integer array height of length n. There are n vertical lines 
# drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, 
# such that the container contains the most water.

# Return the maximum amount of water a container can store.


def get_max_container(heights):
    i = 0
    j = len(heights) - 1

    max_volume = 0

    while i < j:
        volume = min(heights[i], heights[j]) * (j - i)

        if volume > max_volume:
            max_volume = volume
        
        if heights[i] < heights[j]:
            i += 1
        else:
            j -= 1
    
    return max_volume

if __name__ == "__main__":
    heights = [2,3,4,5,18,17,6]
    print(get_max_container(heights))
