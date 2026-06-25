class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        starting_color = image[sr][sc]

        if starting_color == color:
            return image
        
        def DSF(row, col):
            #if out of bound
            if row < 0 or col < 0:
                return 
            if row >= len(image) or col >= len(image[0]):
                return 
            #if not same color -> don't paint
            if image[row][col] != starting_color:
                return

            image[row][col] = color

            DSF(row + 1, col)
            DSF(row - 1, col)
            DSF(row, col + 1)
            DSF(row, col - 1)

        DSF(sr, sc)
        return image