import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
COLORS = [
    (0, 255, 255),  # Cyan
    (255, 255, 0),  # Yellow
    (255, 165, 0),  # Orange
    (0, 0, 255),    # Blue
    (128, 0, 128),  # Purple
    (0, 255, 0),    # Green
    (255, 0, 0)     # Red
]

# Tetrimino shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1, 0], [1, 1, 1]],  # T
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]],  # J
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]]   # Z
]

class Tetrimino:
    def __init__(self, shape):
        self.shape = shape
        self.color = random.choice(COLORS)
        self.x = SCREEN_WIDTH // BLOCK_SIZE // 2 - len(shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

def create_grid(locked_positions={}):
    grid = [[BLACK for _ in range(SCREEN_WIDTH // BLOCK_SIZE)] for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)]
    for (x, y), color in locked_positions.items():
        grid[y][x] = color
    return grid

def draw_grid(surface, grid):
    for y, row in enumerate(grid):
        for x, color in enumerate(row):
            pygame.draw.rect(surface, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    for x in range(SCREEN_WIDTH // BLOCK_SIZE):
        pygame.draw.line(surface, GRAY, (x * BLOCK_SIZE, 0), (x * BLOCK_SIZE, SCREEN_HEIGHT))
    for y in range(SCREEN_HEIGHT // BLOCK_SIZE):
        pygame.draw.line(surface, GRAY, (0, y * BLOCK_SIZE), (SCREEN_WIDTH, y * BLOCK_SIZE))

def valid_space(shape, grid, offset):
    off_x, off_y = offset
    for y, row in enumerate(shape):
        for x, cell in enumerate(row):
            if cell:
                new_x = off_x + x
                new_y = off_y + y
                if new_x < 0 or new_x >= len(grid[0]) or new_y >= len(grid) or grid[new_y][new_x] != BLACK:
                    return False
    return True

def clear_rows(grid, locked_positions):
    cleared = 0
    for y in range(len(grid) - 1, -1, -1):
        if BLACK not in grid[y]:
            cleared += 1
            del grid[y]
            grid.insert(0, [BLACK for _ in range(SCREEN_WIDTH // BLOCK_SIZE)])
    return cleared

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()

    locked_positions = {}
    grid = create_grid(locked_positions)

    current_piece = Tetrimino(random.choice(SHAPES))
    next_piece = Tetrimino(random.choice(SHAPES))

    fall_time = 0
    fall_speed = 0.5
    running = True

    while running:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time / 1000 >= fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not valid_space(current_piece.shape, grid, (current_piece.x, current_piece.y)):
                current_piece.y -= 1
                for y, row in enumerate(current_piece.shape):
                    for x, cell in enumerate(row):
                        if cell:
                            locked_positions[(current_piece.x + x, current_piece.y + y)] = current_piece.color
                current_piece = next_piece
                next_piece = Tetrimino(random.choice(SHAPES))
                if not valid_space(current_piece.shape, grid, (current_piece.x, current_piece.y)):
                    running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece.shape, grid, (current_piece.x, current_piece.y)):
                        current_piece.x += 1
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece.shape, grid, (current_piece.x, current_piece.y)):
                        current_piece.x -= 1
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not valid_space(current_piece.shape, grid, (current_piece.x, current_piece.y)):
                        current_piece.y -= 1
                if event.key == pygame.K_UP:
                    current_piece.rotate()
                    if not valid_space(current_piece.shape, grid, (current_piece.x, current_piece.y)):
                        current_piece.rotate()
                        current_piece.rotate()
                        current_piece.rotate()

        draw_grid(screen, grid)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()