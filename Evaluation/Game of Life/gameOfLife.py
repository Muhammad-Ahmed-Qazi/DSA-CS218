from lifeGrid import LifeGrid
from colorama import Fore, Style, init

# Initialize colorama.
init(autoreset=True)

# Set size of the grid
GRID_WIDTH = 5
GRID_HEIGHT = 5

# Define initial configuration of live cells
INIT_CONFIG = [(1, 1), (1, 2), (2, 2), (3, 2)]
# INIT_CONFIG = [(1, 2), (2, 1), (2, 2), (2, 3)]

# Indicate no. of generations to observe
NUM_GENS = 8

# Prints a text-based grid representation of the game grid
def draw(grid):
    """
    Prints a text-based representation of the game grid, 
    using '✓' for live cells and 'x' for dead cells.
    """
    num_rows = grid.numRows()
    num_cols = grid.numCols()
    
    # 1. Calculate the width for the top/bottom border
    # Each cell takes 2 characters (' ' + '✓' or 'x'). Plus 3 for side borders.
    border_width = num_cols * 2 + 3 
    
    # Print the top border
    print(Fore.WHITE + "\n╔" + "═" * border_width + "╗" + Style.RESET_ALL)

    # 2. Iterate through rows and columns
    for i in range(num_rows):
        # Print the left boundary of the row
        print(Fore.WHITE + "║ ", end=" ") 
        
        for j in range(num_cols):
            cell = grid.cell(i, j)
            if cell == '✓':
                print(Fore.GREEN + cell, end=" ")
            else:
                print(Fore.RED + cell, end=" ") 
        
        # Print the right boundary of the row and a newline
        print(Fore.WHITE + " ║") 

    # Print the bottom border
    print(Fore.WHITE + "╚" + "═" * border_width + "╝")

# Generates the next generation of organisms
def evolve(grid):
    liveCells = list()

    for i in range(grid.numRows()):
        for j in range(grid.numCols()):
            neighbours = grid.numLiveNeighbours(i, j)

            if (grid.isLiveCell(i, j) and neighbours == 2) or (neighbours == 3):
                liveCells.append((i, j))
    print(liveCells)

# Main function
def main():
    # Construct the grid and configure it
    grid = LifeGrid(GRID_WIDTH, GRID_HEIGHT)
    grid.configure(INIT_CONFIG)

    # Play the game
    draw(grid)
    for i in range(NUM_GENS):
        buffer = input(f"Press enter to show Gen. {i + 1}")
        evolve(grid)
        draw(grid)

# Running the program
main()