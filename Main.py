import pygame
import numpy as np
from AI import ai_move

pygame.init()
# 定义界面尺寸
WIDTH,HEIGHT,MARGIN=600,600,50
BOARD_SIZE = 15
GRID_SIZE= (WIDTH-2*MARGIN) /BOARD_SIZE
Radius=GRID_SIZE / 2
BUTTON_WIDTH,BUTTON_HEIGHT  = 120,40
Board =np.full((BOARD_SIZE+1,BOARD_SIZE+1), -1)

# 定义颜色
BLACK = (69, 68, 69)
WHITE = (255, 255, 255)

# 创建界面
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("五子棋")
background_image = pygame.image.load("./board.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
button_rect = pygame.Rect((WIDTH - BUTTON_WIDTH) // 2, HEIGHT - BUTTON_HEIGHT-5, BUTTON_WIDTH, BUTTON_HEIGHT)
# 绘制棋盘
def draw_board():
    screen.blit(background_image, (0, 0))
    for i in range(BOARD_SIZE+1):
        pygame.draw.line(screen, BLACK, (MARGIN+GRID_SIZE * i, MARGIN), (MARGIN+GRID_SIZE * i, HEIGHT-MARGIN))
        pygame.draw.line(screen, BLACK, (MARGIN, MARGIN+GRID_SIZE * i), (WIDTH-MARGIN, MARGIN+GRID_SIZE * i))

# 绘制棋子
def draw_piece(row, col, color):
    pygame.draw.circle(screen, color, (MARGIN+col * GRID_SIZE, MARGIN+row * GRID_SIZE), Radius)

def draw_button():
    pygame.draw.rect(screen, (219,187,153), button_rect)  # 绘制按钮矩形
    font = pygame.font.SysFont('simHei',18)
    text = font.render("重新开始", True, (0,0,0))
    text_rect = text.get_rect(center=button_rect.center)
    screen.blit(text, text_rect)  # 绘制按钮文字

# 游戏主循环
def game_loop():
    running = True
    draw_board()
    draw_button()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 重新开始
                if button_rect.collidepoint(event.pos) and event.button == 1:
                    for i in range(BOARD_SIZE+1):
                        for j in range(BOARD_SIZE+1):
                            Board[i][j]=-1
                    draw_board()
                    draw_button()
                    continue
                else:
                    mouse_pos = pygame.mouse.get_pos()  ##先横后竖
                    col = int((mouse_pos[0]+GRID_SIZE/2-MARGIN) / GRID_SIZE)
                    row = int((mouse_pos[1]+GRID_SIZE/2-MARGIN) / GRID_SIZE)
                    #print("my choose= ",(col,row))
                    if(MARGIN-Radius<mouse_pos[0] and mouse_pos[0]<WIDTH-MARGIN+Radius and MARGIN-Radius<mouse_pos[1] and mouse_pos[1]<=HEIGHT-MARGIN and Board[col][row]==-1):
                        draw_piece(row, col, BLACK)
                        Board[col][row]=1
                        ai_choose=ai_move(Board)
                        #print("ai choose= ",ai_choose)
                        Board[ai_choose[0]][ai_choose[1]]=0
                        draw_piece(ai_choose[1],ai_choose[0],WHITE)
            # 更新界面
            pygame.display.flip()
    pygame.quit()

# 运行游戏
game_loop()