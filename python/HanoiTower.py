# def recursion(n,fr,to,between):
#     if(n == 0):
#         return
#     recursion(n - 1,fr,between,to)
#     print("Chuyển đĩa: " + str(n) + " từ cột " + fr + " sang cột " + to)
#     recursion(n - 1,between,to,fr)

# if __name__ == "__main__":
#     n = int(input())
#     recursion(n,"A","C","B")

import pygame
import sys
import time

# Cấu hình màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_GRAY = (200, 200, 200)

# Cấu hình trò chơi
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
PEG_X_POSITIONS = [200, 400, 600]
PEG_Y_POSITION = 300
DISK_HEIGHT = 20
DISK_COLORS = [RED, GREEN, BLUE]

# Khởi tạo pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tower of Hanoi")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Vẽ các cột
def draw_pegs():
    for x in PEG_X_POSITIONS:
        pygame.draw.rect(screen, BLACK, (x - 5, 100, 10, 200))

# Vẽ các đĩa
def draw_disks(pegs, selected_disk=None, mouse_pos=None):
    for peg_index, peg in enumerate(pegs):
        for disk_index, disk in enumerate(peg):
            if selected_disk == (peg_index, disk_index):
                continue
            disk_width = disk * 30
            color = DISK_COLORS[disk % len(DISK_COLORS)]
            x = PEG_X_POSITIONS[peg_index] - disk_width // 2
            y = PEG_Y_POSITION - (disk_index + 1) * DISK_HEIGHT
            pygame.draw.rect(screen, color, (x, y, disk_width, DISK_HEIGHT))
    if selected_disk and mouse_pos:
        disk_width = selected_disk[1] * 30
        color = DISK_COLORS[selected_disk[1] % len(DISK_COLORS)]
        x = mouse_pos[0] - disk_width // 2
        y = mouse_pos[1] - DISK_HEIGHT // 2
        pygame.draw.rect(screen, color, (x, y, disk_width, DISK_HEIGHT))

# Cập nhật màn hình
def update_screen(pegs, selected_disk=None, mouse_pos=None):
    screen.fill(WHITE)
    draw_pegs()
    draw_disks(pegs, selected_disk, mouse_pos)
    draw_buttons()
    pygame.display.flip()

# Vẽ các nút điều khiển
def draw_buttons():
    solve_button = pygame.Rect(650, 50, 100, 50)
    inc_button = pygame.Rect(650, 120, 50, 50)
    dec_button = pygame.Rect(700, 120, 50, 50)
    pygame.draw.rect(screen, LIGHT_GRAY, solve_button)
    pygame.draw.rect(screen, LIGHT_GRAY, inc_button)
    pygame.draw.rect(screen, LIGHT_GRAY, dec_button)
    screen.blit(font.render("Solve", True, BLACK), (665, 60))
    screen.blit(font.render("+", True, BLACK), (670, 130))
    screen.blit(font.render("-", True, BLACK), (720, 130))

# Thuật toán đệ quy Tháp Hà Nội
def recursion(n, fr, to, between, pegs):
    if n == 0:
        return
    recursion(n - 1, fr, between, to, pegs)
    pegs[to].append(pegs[fr].pop())
    update_screen(pegs)
    time.sleep(0.5)
    recursion(n - 1, between, to, fr, pegs)

# Hàm chính
def main():
    num_disks = 3
    pegs = [list(range(num_disks, 0, -1)), [], []]
    selected_disk = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 650 <= x <= 750 and 50 <= y <= 100:  # Nút "Solve"
                    recursion(num_disks, 0, 2, 1, pegs)
                elif 650 <= x <= 700 and 120 <= y <= 170:  # Nút tăng đĩa
                    num_disks = min(num_disks + 1, 10)
                    pegs = [list(range(num_disks, 0, -1)), [], []]
                elif 700 <= x <= 750 and 120 <= y <= 170:  # Nút giảm đĩa
                    num_disks = max(num_disks - 1, 1)
                    pegs = [list(range(num_disks, 0, -1)), [], []]
                else:
                    for i, peg_x in enumerate(PEG_X_POSITIONS):
                        if abs(x - peg_x) < 50 and pegs[i]:
                            selected_disk = (i, pegs[i][-1])
                            break
            if event.type == pygame.MOUSEBUTTONUP and selected_disk:
                x, y = event.pos
                for i, peg_x in enumerate(PEG_X_POSITIONS):
                    if abs(x - peg_x) < 50:
                        if not pegs[i] or pegs[i][-1] > selected_disk[1]:
                            pegs[i].append(pegs[selected_disk[0]].pop())
                        break
                selected_disk = None
        update_screen(pegs, selected_disk, pygame.mouse.get_pos())
        clock.tick(30)

if __name__ == '__main__':
    main()
