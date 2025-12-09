import random
import sys
import os

# Set random seed as specified
random.seed(1234)

def layMines(PMineField: list[list[int]], PMines: int) -> None:
    """
    Randomly places mines to the PMineField.
    The "PMineField" is pre-initialized 2d matrix with zeros.
    """
    rows = len(PMineField)
    cols = len(PMineField[0]) if rows > 0 else 0
    total_cells = rows * cols
    
    # Safety check: don't place more mines than available cells
    if PMines > total_cells:
        PMines = total_cells
    
    # Generate all possible positions
    all_positions = [(r, c) for r in range(rows) for c in range(cols)]
    
    # Randomly select mine positions
    mine_positions = random.sample(all_positions, PMines)
    
    # Place mines
    for row, col in mine_positions:
        PMineField[row][col] = 9

def calculateNearbys(PMineField: list[list[int]]) -> None:
    """
    Calculates nearby mines for each cell in the minefield.
    Expects 2d-matrix with mines already placed (9 represents mine).
    """
    rows = len(PMineField)
    cols = len(PMineField[0]) if rows > 0 else 0
    
    # Directions for 8 neighbors
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    
    # Create a copy to avoid modifying while calculating
    temp_field = [row[:] for row in PMineField]
    
    for r in range(rows):
        for c in range(cols):
            # Skip mines
            if temp_field[r][c] == 9:
                continue
            
            mine_count = 0
            
            # Check all 8 neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check if neighbor is within bounds
                if 0 <= nr < rows and 0 <= nc < cols:
                    if temp_field[nr][nc] == 9:
                        mine_count += 1
            
            # Update the original field
            PMineField[r][c] = mine_count

def generateMinefield(
        PMineField: list[list[int]],
        PRows: int,
        PCols: int,
        PMines: int) -> None:
    """
    Takes empty "PMineField" list and amount of rows, columns and mines as parameters.
    Creates a complete minefield with mines and calculated nearby counts.
    """
    # 1. Clear the list
    PMineField.clear()
    
    # 2. Initialize 2D matrix with zeros
    for i in range(PRows):
        PMineField.append([])
        for _ in range(PCols):
            PMineField[i].append(0)
    
    # 3. Lay mines
    layMines(PMineField, PMines)
    
    # 4. Calculate nearbys
    calculateNearbys(PMineField)

# Helper functions for the menu system
def display_board(board: list[list[int]]) -> None:
    """Display the minefield board in a readable format."""
    if not board:
        print("No board generated yet.")
        return
    
    rows = len(board)
    cols = len(board[0]) if rows > 0 else 0
    
    print(f"\nMinefield ({rows}x{cols}):")
    print("   " + " ".join(f"{c:2}" for c in range(cols)))
    print("  " + "---" * cols + "-")
    
    for r in range(rows):
        print(f"{r:2}|", end="")
        for c in range(cols):
            value = board[r][c]
            if value == 9:
                print(" 🚫", end="")  # Mine symbol
            elif value == 0:
                print(" · ", end="")  # Empty cell
            else:
                print(f" {value} ", end="")
        print()

def save_board_to_file(board: list[list[int]], filename: str) -> bool:
    """Save board to file in comma-separated format."""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for row in board:
                # Convert each number to string and join with commas
                line = ','.join(str(cell) for cell in row)
                file.write(line + '\n')
        return True
    except Exception as e:
        print(f"Error saving file: {e}")
        return False

def print_menu() -> None:
    """Print the main menu."""
    print("\n" + "="*40)
    print("MINESWEEPER BOARD GENERATOR")
    print("="*40)
    print("1. Generate minesweeper board")
    print("2. Show generated board")
    print("3. Save board to file")
    print("0. Exit")
    print("-"*40)

def get_integer_input(prompt: str, min_val: int = 1, max_val: int = 100) -> int:
    """Get valid integer input from user."""
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Value must be between {min_val} and {max_val}")
        except ValueError:
            print("Please enter a valid integer")

def main() -> None:
    """
    Create a menu-driven program where user can generate boards for the
    Minesweeper game.
    """
    current_board = []
    board_generated = False
    
    while True:
        print_menu()
        
        try:
            choice = input("Enter your choice (0-3): ").strip()
            
            if choice == '0':
                print("\nExiting program. Goodbye!")
                break
                
            elif choice == '1':
                # Option 1: Generate minesweeper board
                print("\n--- Generate New Board ---")
                
                rows = get_integer_input("Enter number of rows (1-50): ", 1, 50)
                cols = get_integer_input("Enter number of columns (1-50): ", 1, 50)
                
                max_mines = rows * cols - 1  # Leave at least one safe cell
                mines_prompt = f"Enter number of mines (1-{max_mines}): "
                mines = get_integer_input(mines_prompt, 1, max_mines)
                
                print(f"\nGenerating {rows}x{cols} board with {mines} mines...")
                generateMinefield(current_board, rows, cols, mines)
                board_generated = True
                
                print(f"Board generated successfully!")
                display_board(current_board)
                
            elif choice == '2':
                # Option 2: Show generated board
                if not board_generated:
                    print("\nNo board has been generated yet. Please generate a board first (option 1).")
                else:
                    display_board(current_board)
                    
            elif choice == '3':
                # Option 3: Save board
                if not board_generated:
                    print("\nNo board has been generated yet. Please generate a board first (option 1).")
                else:
                    filename = input("\nEnter filename to save (e.g., 'minesweeper_board.txt'): ").strip()
                    if not filename:
                        print("Filename cannot be empty.")
                        continue
                    
                    # Add .txt extension if not present
                    if not filename.lower().endswith('.txt'):
                        filename += '.txt'
                    
                    if save_board_to_file(current_board, filename):
                        print(f"Board saved successfully to '{filename}'")
                    else:
                        print("Failed to save board.")
                        
            else:
                print("\nInvalid choice. Please enter a number between 0 and 3.")
                
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Exiting...")
            break
        except EOFError:
            print("\n\nEnd of input. Exiting...")
            break
        except Exception as e:
            print(f"\nAn error occurred: {e}")

# Test function to verify the implementation matches the example
def test_implementation():
    """Test function to verify the implementation produces the expected output."""
    print("Testing Minesweeper implementation...")
    
    # Create a test board matching the example dimensions
    test_board = []
    generateMinefield(test_board, 7, 6, 10)  # Should place exactly 10 mines
    
    print("\nGenerated board:")
    for row in test_board:
        print(row)
    
    # Display in the format shown in the example
    print("\nFormatted output:")
    for i, row in enumerate(test_board):
        row_str = ','.join(str(cell) for cell in row)
        print(f"{row_str} # row {i+1}")
    
    return test_board

if __name__ == "__main__":
    # Uncomment the next line to run the test
    # test_implementation()
    
    # Run the main program
    main()