#LeetCode: 1725. Number Of Rectangles That Can Form The Largest Square
#Runtime: 155 ms, Beats 87.13%
#Memory: 16.95 MB, Beats 98.10%

def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        minLens = [0] * len(rectangles)            #Initialize list of zeroes
        for i, rect in enumerate(rectangles):      #Loop to get lower value of each rectangle pair
            if rect[0] < rect[1]:
                minLens[i] = rect[0]
            else:
                minLens[i] = rect[1]
        
        return minLens.count(max(minLens))         #Return the count of the highest value in minLens
