import pygame
import sys
import sudoku
def gameStart():
    # Initialize Pygame
    pygame.init()

    # Constants
    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    BUTTON_WIDTH, BUTTON_HEIGHT = 200, 100
    BLUE = (0, 0, 255)

    # Set up the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("sudoku.py")

    # Load the exit button image
    exit_img = pygame.image.load('Restart.jpg')
    exit_img = pygame.transform.scale(exit_img, (BUTTON_WIDTH, BUTTON_HEIGHT))

    # Function to draw the exit button
    def draw_exit_button():
        x = SCREEN_WIDTH // 2 - BUTTON_WIDTH // 2
        y = SCREEN_HEIGHT // 2 - BUTTON_HEIGHT // 2
        screen.blit(exit_img, (x, y))
        return pygame.Rect(x, y, BUTTON_WIDTH, BUTTON_HEIGHT)

    # Main loop
    running = True
    while running:
        screen.fill(BLUE)

        # Draw "Game Won" text
        font = pygame.font.Font(None, 74)
        text = font.render('Game Over :(', True, (255, 255, 255))
        text_rect = text.get_rect(center=(SCREEN_WIDTH//2, 50))
        screen.blit(text, text_rect)

        # Draw exit button
        exit_button = draw_exit_button()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if exit_button.collidepoint(mouse_pos):
                    running = False

        pygame.display.flip()

    pygame.quit()
    sudoku.run()


if __name__=="__main__":
    gameStart()