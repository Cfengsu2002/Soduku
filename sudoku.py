import pygame, sys
import button
import game

def run():
    CHIP_FONT=2 # Constant
    LINE_COLOR=(139, 69, 19)
    square_size=50
    BG_COLOR=(245, 245, 220)
    HEIGHT=515
    WIDTH=450
    BOARD_ROWS = 9
    BOARD_COLS = 9
    removed_size=30
    CHIP_FONT=(0,0,0)
    # creating game window
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Sudoku")
    # Font used
    font1 = pygame.font.SysFont("arialblack", 25)
    font2 = pygame.font.SysFont("arialblack", 20)

    Text_color = (0, 0, 0)
    # load button images
    easy_mode = pygame.image.load('original-E616BDA1-32FC-4C94-9241-32CC8AC2E009.jpeg').convert_alpha()
    normal_mode=pygame.image.load('original-FB333092-2F5B-4C9B-A64A-D2C110349237.jpeg').convert_alpha()
    difficult_mode=pygame.image.load('original-9303CD20-6C22-4F37-8A96-EED6AD93A2AE.jpeg').convert_alpha()
    # button class
    #create button instances
    easy_mode_button = button.Button(160,240, easy_mode, 0.214)
    normal_mode_button = button.Button(160, 310, normal_mode, 0.2)
    difficult_mode_button = button.Button(160,380, difficult_mode, 0.217)
    easy_mode_button.draw(screen)
    normal_mode_button.draw(screen)
    difficult_mode_button.draw(screen)
    def draw_text(text, font, text_col, x, y):
        img= font.render(text, True, text_col)
        screen.blit(img, (x, y))

    run = True


    def generateGameMode(difficultyLevel:str):
        pygame.quit()
        if(difficultyLevel=="easy"):
            print("easy Mode")
            game.createGameLoop(30)
        elif(difficultyLevel=="normal"):
            print("easy Mode")
            game.createGameLoop(40)
        elif(difficultyLevel=="hard"):
            print("easy Mode")
            game.createGameLoop(50)



    while run:
        screen.fill((245, 245, 220))
        if easy_mode_button.draw(screen):
            generateGameMode("easy")
        if normal_mode_button.draw(screen):
            generateGameMode("normal")
        if difficult_mode_button.draw(screen):
            generateGameMode("hard")
        draw_text("Welcome to Sudoku", font1, Text_color,86,60)
        draw_text("Select Game Mode", font2, Text_color,118,130)
        easy_mode_button.draw(screen)
        normal_mode_button.draw(screen)
        difficult_mode_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
    pygame.quit()

if __name__=="__main__":
    run()