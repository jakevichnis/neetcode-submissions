class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)
        for row in range(9):
            for column in range(9):
                digit = board[row][column]
                if digit == ".":
                    continue
                if digit in rows[row] or digit in columns[column] or digit in boxes[(row//3, column//3)]:
                    return False
                columns[column].add(digit)
                boxes[(row//3, column//3)].add(digit)
                rows[row].add(digit)
        return True
                
                