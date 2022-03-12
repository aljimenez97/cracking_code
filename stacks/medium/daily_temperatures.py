# https://leetcode.com/problems/daily-temperatures/

# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have 
# to wait after the ith day to get a warmer temperature. If there is no future 
# day for which this is possible, keep answer[i] == 0 instead.

def warm_temps(temps):
    out = [0] * len(temps)
    stack = []

    for i, t in enumerate(temps):
        while stack and stack[-1][0] < t:
            _, idx = stack.pop()
            out[idx] = i - idx
        stack.append((t, i))

    return out

if __name__ == "__main__":
    temperatures = [30,40,50,60]
    print(warm_temps(temperatures))