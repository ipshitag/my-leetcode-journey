"""
Note:
This is based on the slope formula, which states that the slope of a line through two points (x1, y1) and (x2, y2) is given by (y2 - y1) / (x2 - x1).
This theorem is important because it helps us determine whether three points are collinear or not. If the slopes of the line segments connecting the points are equal, then the points are collinear.

Space Complexity: O(1)
Time Complexity: O(n)
"""

from typing import List
def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
    """
    Given an array coordinates of integer points where coordinates[i] = [x, y] represents a point on the X-Y plane, 
    return true if these points all lie on the same straight line in the X-Y plane.
    """
    if len(coordinates) < 3:
        return True
    x0, y0 = coordinates[0]
    x1, y1 = coordinates[1]
    for i in range(2, len(coordinates)):
        x, y = coordinates[i]
        if (y - y0) * (x1 - x0) != (y1 - y0) * (x - x0):
            return False
    return True