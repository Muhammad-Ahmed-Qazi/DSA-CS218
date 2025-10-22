class LifeGrid:
    # Defining constants to represent cells states
    DEAD_CELL = 'x'
    LIVE_CELL = '✓'

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

    def numRows(self): return self.rows
    def numCols(self): return self.cols
    def cell(self, i, j): return self.grid[i][j]

    def clearCell(self, row, col):
        self.grid[row][col] = self.DEAD_CELL

    def setCell(self, row, col):
        self.grid[row][col] = self.LIVE_CELL

    def configure(self, coordList):
        for i in range(self.rows):
            for j in range(self.cols):
                cell = (i, j)
                if cell in coordList:
                    self.setCell(i, j)
                else:
                    self.clearCell(i, j)
    
    def isLiveCell(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.grid[row][col] == self.LIVE_CELL

    def numLiveNeighbours(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols: # Valid range of grid
            alive = 0

            for i in range(row - 1, row + 2):
                for j in range(col - 1, col + 2):
                    if i == row and j == col: # Skipping the centre cell
                        continue

                    if 0 <= i < self.rows and 0 <= j < self.cols:
                        alive += 1 if self.isLiveCell(i, j) else 0
        return alive
    