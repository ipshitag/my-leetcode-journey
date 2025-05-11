from typing import List
def isRobotBounded(instructions: str) -> bool:
    """
    :type instructions: str
    :rtype: bool
    """
    # Directions: North, East, South, West
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    x, y = 0, 0
    direction_index = 0

    for instruction in instructions:
        if instruction == 'G':
            x += directions[direction_index][0]
            y += directions[direction_index][1]
        elif instruction == 'L':
            direction_index = (direction_index - 1) % 4
        elif instruction == 'R':
            direction_index = (direction_index + 1) % 4

    # Check if the robot is back at the origin or facing a different direction
    return (x == 0 and y == 0) or direction_index != 0