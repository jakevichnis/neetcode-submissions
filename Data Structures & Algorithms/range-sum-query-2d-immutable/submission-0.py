class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        if not matrix or not matrix[0]:
            return

        i, j = len(matrix), len(matrix[0])
        # initialize prefix sum matrix with size (i + 1) x (j + 1) to avoid boundary checks
        self.prefix = [[0] * (j + 1) for _ in range(i + 1)]

        for r in range(i):
            for c in range(j):
                self.prefix[r + 1][c + 1] = (
                    matrix[r][c]
                    + self.prefix[r][c + 1]
                    + self.prefix[r + 1][c]
                    - self.prefix[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # get the sum of the four rectangles
        bottom_right = self.prefix[row2 + 1][col2 + 1]
        top_above = self.prefix[row1][col2 + 1]
        left_side = self.prefix[row2 + 1][col1]
        top_left = self.prefix[row1][col1]

        return bottom_right - top_above - left_side + top_left
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)