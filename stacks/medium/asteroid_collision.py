# https://leetcode.com/problems/asteroid-collision/

# We are given an array asteroids of integers representing asteroids in a row.

# For each asteroid, the absolute value represents its size, and the sign 
# represents its direction (positive meaning right, negative meaning left). 
# Each asteroid moves at the same speed.

# Find out the state of the asteroids after all collisions. If two asteroids 
# meet, the smaller one will explode. If both are the same size, both will explode. 
# Two asteroids moving in the same direction will never meet.

def asteroid_collision(asteroids):
    stack = []
    out = []

    for asteroid in asteroids:
        if asteroid > 0:
            stack.append(asteroid)
        else:
            while stack and stack[-1] < abs(asteroid):
                stack.pop()
            if stack and stack[-1] == abs(asteroid):
                stack.pop()
            elif not stack:
                out.append(asteroid)
    return out + stack

if __name__ == "__main__":
    asteroids= [5, 10, -5]
    print(asteroid_collision(asteroids))