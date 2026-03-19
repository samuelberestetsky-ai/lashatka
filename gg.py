import pygame

# Constants
WINDOW_SIZE = 480
BOARD_SIZE = 8
CELL_SIZE = WINDOW_SIZE // BOARD_SIZE
WHITE = (240, 217, 181)
BLACK = (181, 136, 99)
RED = (200, 50, 50)
BLUE = (50, 50, 200)

# Initialize Pygame
pygame.init() 
window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Checkers Game")
clock = pygame.time.Clock()

# Draw the board
def draw_board():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(window, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Draw pieces
def draw_pieces(board):
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == "player":
                pygame.draw.circle(window, RED, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)
            elif board[row][col] == "bot":
                pygame.draw.circle(window, BLUE, (col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 3)

# Initialize the board with pieces
def initialize_board():
    board = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    for row in range(3):
        for col in range(BOARD_SIZE):
            if (row + col) % 2 != 0:
                board[row][col] = "bot"
    for row in range(5, 8):
        for col in range(BOARD_SIZE):
            if (row + col) % 2 != 0:
                board[row][col] = "player"
    return board

# Game loop
def main():
    board = initialize_board()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_board()
        draw_pieces(board)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

# Run the game
main()