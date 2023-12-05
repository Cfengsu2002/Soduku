import pygame, sys
from copy import copy, deepcopy

import button
import gameStart
import gameWon
import sudoku_generator

CHIP_FONT = 2  # Constant
LINE_COLOR = (139, 69, 19)
square_size = 50
BG_COLOR = (245, 245, 220)
HEIGHT = 515
WIDTH = 450
CHIP_FONT = (0, 0, 0)


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.isGuess = False

    def set_cell_value(self, value):
        Cell.value = value
        Cell.draw()
        pygame.display.update()

    def set_sketched_value(self, value):
        self.value = value

    def draw(self):
        pass


def setToNegativeIfExist(val: int):
    if (val > 0):
        return -1
    else:
        return val


class Board:
    def __init__(self, width: int, height: int, screen, difficulty: int):

        # 先設定好board
        self.BOARD_ROWS = self.BOARD_COLS = 9
        self.difficulty = difficulty
        self.orignialBoards = sudoku_generator.generate_sudoku(self.BOARD_ROWS, self.difficulty)
        self.board = deepcopy(self.orignialBoards[1])
        self.totalInputs = 0

        self.guesses = [[setToNegativeIfExist(item) for item in row] for row in self.board]
        # 接着設定畫面的窗戶
        self.width = width
        self.height = height
        self.screen = screen
        self.selected_cell = [-1, -1]

        pygame.display.set_caption("Sudoku")
        self.screen.fill(BG_COLOR)

        # initialize game state
        self.game_over = False

        self.draw()

    def draw(self):  # this will show the game

        self.screen.fill(BG_COLOR)
        self.square_size = 50
        for i in range(1, 10):
            pygame.draw.line(self.screen, LINE_COLOR, (0, i * self.square_size), (450, i * self.square_size),
                             2)  # horizontal line
            pygame.draw.line(self.screen, LINE_COLOR, (i * self.square_size, 0), (i * self.square_size, 450),
                             2)  # vertical line
        for i in range(0, 4):
            pygame.draw.line(self.screen, LINE_COLOR, (0, i * self.square_size * 3), (450, i * self.square_size * 3),
                             10)  # horizontal line
            pygame.draw.line(self.screen, LINE_COLOR, (i * self.square_size * 3, 0), (i * self.square_size * 3, 450),
                             10)  # vertical line

        chip_font = pygame.font.Font(None, 30)
        if self.selected_cell[0] >= 0:
            pygame.draw.rect(self.screen, (200, 0, 200), (
            self.selected_cell[0] * square_size, self.selected_cell[1] * square_size, square_size, square_size))

        for i in range(0, self.BOARD_ROWS):
            for j in range(0, self.BOARD_COLS):
                if self.board[i][j] != 0:
                    chip_x_surf = chip_font.render(str(self.board[i][j]), 0, CHIP_FONT)
                    chip_x_rect = chip_x_surf.get_rect(
                        center=(i * square_size + square_size // 2, j * square_size + square_size // 2))
                    self.screen.blit(chip_x_surf, chip_x_rect)
                if self.guesses[i][j] > 0:
                    chip_x_surf = chip_font.render(str(self.guesses[i][j]), 1, (255, 0, 0))
                    chip_x_rect = chip_x_surf.get_rect(
                        center=(i * square_size + square_size // 2, j * square_size + square_size // 2))
                    self.screen.blit(chip_x_surf, chip_x_rect)

    def handleGuess(self, guessValue):
        if self.guesses[self.selected_cell[0]][self.selected_cell[1]] >= 0:
            self.guesses[self.selected_cell[0]][self.selected_cell[1]] = guessValue

    def checkBoard(self):
        row:int =0
        column:int =0
        while row<self.BOARD_ROWS:
            while column<self.BOARD_COLS:
                if(self.board[row][column]!=self.orignialBoards[0][row][column]):
                    return False
                print(row,column,self.board[row][column],self.orignialBoards[0][row][column])
                column+=1
            column=0
            print()
            row+=1

        return True
    def enterValue(self):
        if self.guesses[self.selected_cell[0]][self.selected_cell[1]] > 0:
            self.board[self.selected_cell[0]][self.selected_cell[1]] = self.guesses[self.selected_cell[0]][
                self.selected_cell[1]]
            self.guesses[self.selected_cell[0]][self.selected_cell[1]] = -1
            self.totalInputs+=1
        if(self.totalInputs==self.difficulty):
            if(self.checkBoard()):
                print("Success")
                gameWon.gameWOn()
            else:
                print("Failed")
                gameStart.gameStart()


    def update_board(self, event, otherElements: list):
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not self.game_over:
            x, y = event.pos
            row = y // square_size
            col = x // square_size
            if (0 <= row < self.BOARD_ROWS) and (0 <= col < self.BOARD_COLS):
                self.select_cell(row, col)
        elif event.type == pygame.KEYDOWN:

            if self.selected_cell[0] >= 0 and event.unicode.isdigit():
                number = int(event.unicode)
                self.handleGuess(number)
            elif event.unicode == "\b":  ##backspace
                if self.selected_cell[0] >= 0:
                    self.handleGuess(0)

            elif event.unicode == "\r":  ##enter
                if self.selected_cell[0] >= 0:
                    self.enterValue()
            elif event.key == pygame.K_DOWN:
                row = self.selected_cell[1] + 1
                col = self.selected_cell[0]
                if (0 <= row < self.BOARD_ROWS) and (0 <= col < self.BOARD_COLS):
                    self.select_cell(row, col)
            elif event.key == pygame.K_UP:
                row = self.selected_cell[1] - 1
                col = self.selected_cell[0]
                if (0 <= row < self.BOARD_ROWS) and (0 <= col < self.BOARD_COLS):
                    self.select_cell(row, col)
            elif event.key == pygame.K_LEFT:
                row = self.selected_cell[1]
                col = self.selected_cell[0] - 1
                if (0 <= row < self.BOARD_ROWS) and (0 <= col < self.BOARD_COLS):
                    self.select_cell(row, col)
            elif event.key == pygame.K_RIGHT:
                row = self.selected_cell[1]
                col = self.selected_cell[0] + 1
                if (0 <= row < self.BOARD_ROWS) and (0 <= col < self.BOARD_COLS):
                    self.select_cell(row, col)

        self.draw()

        for element in otherElements:
            element.draw(self.screen)

        pygame.display.update()

    # def mark_diffiulty(WIDTH, HEIGHT, removed_size=30):  # 創造一個按照removed_size來設定difficulty的Board
    #    return Board(WIDTH, HEIGHT, removed_size)

    def select_cell(self, col, row):
        self.selected_cell = (row, col)
        print("selected cell", self.selected_cell)
        print("selected Cell value:", self.board[row][col])

    def restartBoard(self):
        self.draw()
        return

    def resetBoard(self):
        self.board = deepcopy(self.orignialBoards[1])
        self.guesses = [[setToNegativeIfExist(item) for item in row] for row in self.board]
        self.totalInputs = 0
        self.draw()
        return


def createGameLoop(numberOfRemovedCells: int = 1) -> None:
    # creating game window
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    # Font used
    font1 = pygame.font.SysFont("arialblack", 25)
    font2 = pygame.font.SysFont("arialblack", 20)

    Text_color = (0, 0, 0)
    # load button images
    exit_image = pygame.image.load('Exit.jpg').convert_alpha()
    restart_image = pygame.image.load('Restart.jpg').convert_alpha()

    reset_image = pygame.image.load('restart.jpg').convert_alpha()
    # button class
    # create button instances
    y_height = HEIGHT - 60

    exit_button = button.Button(WIDTH / 5 - 50, y_height, exit_image, 0.214)
    resart_button = button.Button(WIDTH / 2 - 50, y_height, restart_image, 0.2)
    reset_button = button.Button(WIDTH * 4 / 5 - 50, y_height, reset_image, 0.217)

    board = Board(WIDTH, HEIGHT, screen, numberOfRemovedCells)
    while True:
        for event in pygame.event.get():
            if exit_button.draw(screen):
                exit(0)
            elif resart_button.draw(screen):
                print("restart clicked")
                board = Board(WIDTH, HEIGHT, screen, numberOfRemovedCells)
            elif reset_button.draw(screen):
                print("reset clicked")
                board.resetBoard()
            else:
                board.update_board(event, [exit_button, reset_button, resart_button])


if __name__ == '__main__':
    createGameLoop()
