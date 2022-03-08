# https://leetcode.com/problems/robot-bounded-in-circle/

# On an infinite plane, a robot initially stands at (0, 0) and faces north. Note that:

# The north direction is the positive direction of the y-axis.
# The south direction is the negative direction of the y-axis.
# The east direction is the positive direction of the x-axis.
# The west direction is the negative direction of the x-axis.
# The robot can receive one of three instructions:

# "G": go straight 1 unit.
# "L": turn 90 degrees to the left (i.e., anti-clockwise direction).
# "R": turn 90 degrees to the right (i.e., clockwise direction).
# The robot performs the instructions given in order, and repeats them forever.

# Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

def circle_exists(instructions):
    orientation = "N"
    position = (0,0)

    moves_dict = {
        "N": (0, 1),
        "E": (1, 0),
        "S": (0, -1),
        "W": (-1, 0)
    }

    left_turn_dict = {
        "N": "W",
        "E": "N",
        "S": "E",
        "W": "S"  
    }

    right_turn_dict = {
        "N": "E",
        "E": "S",
        "S": "W",
        "W": "N"  
    }

    for instruction in instructions*4:
        if instruction == "G":
            dx, dy = moves_dict[orientation]
            position = (position[0] + dx, position[1] + dy)
        if instruction == "L":
            orientation = left_turn_dict[orientation]
        if instruction == "R":
            orientation = right_turn_dict[orientation]

    return True if position == (0,0) else False

if __name__ == "__main__":
    instructions = "GL"
    print(circle_exists(instructions))