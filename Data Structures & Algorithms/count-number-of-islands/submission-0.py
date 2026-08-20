class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # up, left, right, down
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        # set up structure
        ROWS, COLS = len(grid), len(grid[0])
        # our island counter
        islands = 0
        # dfs algorithm
        def dfs(row, col):
            # edge case condition (if it goes beyond the grind boundaries)
            if (row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == "0"):
                return
            # as per the question, "0" is assigned to non-islands
            grid[row][col] = "0"
            # ?
            for dir_row, dir_col in directions:
                dfs(row + dir_row, col + dir_col)
        # run the algorithm nested so it covers 2d
        for row in range(ROWS):
            for col in range(COLS):
                # if we have found an island node, in this case its marked as "1"
                if grid[row][col] == "1":
                    dfs(row, col)
                    islands += 1
        return islands


        