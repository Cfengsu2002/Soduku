import pygame, sys
import button
import sudoku_generator

# Constants for visual elements
CHIP_FONT = 2
LINE_COLOR = (139, 69, 19)  # Brown color for grid lines
square_size = 50  # Size of each square in the grid
BG_COLOR = (245, 245, 220)  # Background color (beige)
HEIGHT = 515
WIDTH = 450
BOARD_ROWS = 9
BOARD_COLS = 9
CHIP_FONT = (0, 0, 0)  # Font color for numbers

# Cell class for each square in the Sudoku grid
class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen

    def set_cell_value(self, value):
        # Set the value of the cell and update display
        Cell.value = value
        Cell.draw()
        pygame.display.update()

    def set_sketched_value(self, value):
        # Set a temporary value (for user input)
        self.value = value

    def draw(self):
        # Method to draw the cell (to be implemented)
        pass

# Board class for the Sudoku board
class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.selected_cell = None

    def draw(self):
        # Draw the Sudoku grid
        self.square_size = 50
        # Draw grid lines
        for i in range(1, 10):
            # Horizontal lines
            pygame.draw.line(self.screen, LINE_COLOR, (0, i * self.square_size), (450, i * self.square_size), 2)
            # Vertical lines
            pygame.draw.line(self.screen, LINE_COLOR, (i * self.square_size, 0), (i * self.square_size, 450), 2)

        # Draw thicker lines to separate 3x3 squares
        for i in range(0, 4):
            # Horizontal lines
            pygame.draw.line(self.screen, LINE_COLOR, (0, i * self.square_size * 3), (450, i * self.square_size * 3), 10)
            # Vertical lines
            pygame.draw.line(self.screen, LINE_COLOR, (i * self.square_size * 3, 0), (i * self.square_size * 3, 450), 10)

        # Generate a Sudoku board and display the numbers
        board = sudoku_generator.generate_sudoku(9, 30)
        chip_font = pygame.font.Font(None, 30)
        for i in range(0, BOARD_ROWS):
            for j in range(0, BOARD_COLS):
                if board[i][j] != 0:
                    chip_x_surf = chip_font.render(str(board[i][j]), None, CHIP_FONT)
                    chip_x_rect = chip_x_surf.get_rect(center=(i * square_size + square_size // 2, j * square_size + square_size // 2))
                    screen.blit(chip_x_surf, chip_x_rect)

    def update_board(self):
        # Update the display
        pygame.display.update()

    @classmethod
    def mark_difficulty(cls, width, height, screen, removed_size=30):
        # Create a board with specific difficulty
        return cls(width, height, screen, removed_size)

    def select_cell(self, row, col):
        # Select a cell on the board
        self.selected_cell = (row, col)

# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku")

# Fonts for text
font1 = pygame.font.SysFont("arialblack", 25)
font2 = pygame.font.SysFont("arialblack", 20)
Text_color = (0, 0, 0)

# Load images for buttons and create button instances
easy_mode = pygame.image.load('original-E616BDA1-32FC-4C94-9241-32CC8AC2E009.jpeg').convert_alpha()
normal_mode = pygame.image.load('original-FB333092-2F5B-4C9B-A64A-D2C110349237.jpeg').convert_alpha()
difficult_mode = pygame.image.load('original-9303CD20-6C22-4F37-8A96-EED6AD93A2AE.jpeg').convert_alpha()

easy_mode_button = button.Button(160, 240, easy_mode, 0.214)
normal_mode_button = button.Button(160, 310, normal_mode, 0.2)
difficult_mode_button = button.Button(160, 380, difficult_mode, 0.217)

# Function to draw text on screen
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# Main game loop
run = True
while run:
    screen.fill(BG_COLOR)

    # Button interactions
    if easy_mode_button.draw(screen):
        print('Easy Mode')
    if normal_mode_button.draw(screen):
        print('Normal Mode')
    if difficult_mode_button.draw(screen):
        print('Difficult Mode')

    # Display text
    draw_text("Welcome to Sudoku", font1, Text_color, 86, 60)
    draw_text("Select Game Mode", font2, Text_color, 118, 130)

    # Draw buttons
    easy_mode_button.draw(screen)
    normal_mode_button.draw(screen)
    difficult_mode_button.draw(screen)

    # Handle quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
