#LeetCode: 1232. Check If It Is a Straight Line
#Runtime: 59ms, Beats 66.75%
#Memory: 16.99MB, Beats 82.77%

#Checks if all coordinates fall on the same line, uses equation y-y0 = (dy/dx)(x-x0)

def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
    if len(coordinates) == 2:
        return True
    x0, y0 = coordinates[0]
    x1, y1 = coordinates[1]
    dy, dx = y1-y0, x1-x0
    for x,y in coordinates[1:]:
        if dx * (y - y0) != dy * (x-x0):
            return False
    return True
