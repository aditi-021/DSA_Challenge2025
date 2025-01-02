class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:

        nearX = max(x1, min(x2, xCenter))
        nearY = max(y1, min(y2, yCenter))

        distX = nearX - xCenter
        distY = nearY - yCenter

        return pow(distX,2)+pow(distY,2) <= pow(radius, 2)
