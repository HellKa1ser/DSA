# def is_valid(row,col,board,n):
#     for i in range(n):
#         if board[row][i] == 1 or board[i][col] == 1:
#             return False
#     for i in range(n):
#         for j in range(n):
#             if (i+j == row+col or i-j == row-col) and board[i][j] == 1:
#                 return False
#     return True
#
# def recursion(board,col,n):
#     if(col == n):
#         for row in board:
#             print(row)
#         print('-------------------------')
#         return
#     for i in range(n):
#         if is_valid(i,col,board,n):
#             board[i][col] = 1
#             if recursion(board,col+1,n):
#                 return True
#             board[i][col] = 0
#     return False
# if __name__ == "__main__":
#     n = int(input())
#     board = [[0 for i in range(n)] for j in range(n)]
#     if recursion(board,0,n):
#         for i in range(n):
#             print(board[i])


import pygame
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

SIZE = 600
MARGIN = 5

solutions = []
current_index = 0

def is_valid(row, col, board, n):
    for i in range(n):
        if board[row][i] == 1 or board[i][col] == 1:
            return False
    for i in range(n):
        for j in range(n):
            if (i + j == row + col or i - j == row - col) and board[i][j] == 1:
                return False
    return True

def recursion(board, col, n):
    global solutions
    if col == n:
        solutions.append([row[:] for row in board])
        return
    for i in range(n):
        if is_valid(i, col, board, n):
            board[i][col] = 1
            recursion(board, col + 1, n)
        board[i][col] = 0

pygame.init()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)

n = int(input('Nhập số lượng quân hậu (n x n): '))
board = [[0 for _ in range(n)] for _ in range(n)]
recursion(board, 0, n)

screen = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption('N-Queen Visualization')
cell_size = SIZE // n

queen_image = pygame.image.load('queen.png')
queen_image.set_colorkey((255, 255, 255))  # Xóa màu nền trắng
queen_image = pygame.transform.scale(queen_image, (cell_size, cell_size))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                current_index = (current_index + 1) % len(solutions)
            elif event.key == pygame.K_DOWN:
                current_index = (current_index - 1) % len(solutions)

    screen.fill(WHITE)
    board = solutions[current_index]

    for row in range(n):
        for col in range(n):
            color = BLACK if (row + col) % 2 == 0 else WHITE
            pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))
            if board[row][col] == 1:
                screen.blit(queen_image, (col * cell_size, row * cell_size))

    text = font.render(f'Solution: {current_index + 1}/{len(solutions)}', True, GREEN)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(10)
