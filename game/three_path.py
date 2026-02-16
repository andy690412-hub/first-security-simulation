import pygame
import sys
import random

# --------------------
# 초기화
# --------------------
pygame.init()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("1인 1주제 미니게임")

# 색상
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)

# 폰트
font_title = pygame.font.SysFont("malgungothic", 36, bold=True)
font_button = pygame.font.SysFont("malgungothic", 28)
font_small = pygame.font.SysFont("malgungothic", 22)

# 버튼 이미지 (파일 그대로 사용)
button_img = pygame.image.load("button_green.jpg")
button_img = pygame.transform.scale(button_img, (400, 80))

# --------------------
# 버튼 클래스
# --------------------
class ImageButton:
    def __init__(self, text, x, y, image, action=None):
        self.text = text
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.action = action

    def draw(self):
        screen.blit(self.image, self.rect)
        text_surf = font_button.render(self.text, True, BLACK)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def click(self, pos):
        if self.rect.collidepoint(pos) and self.action:
            self.action()

# --------------------
# 경로1: 지뢰찾기
# --------------------
def play_minesweeper():
    global state
    size = 10
    mine_x, mine_y = random.randint(0, size-1), random.randint(0, size-1)
    attempts = 10
    cell_size = 40
    clicked_cells = set()
    result = None

    while result is None:
        screen.fill(WHITE)
        msg = font_small.render(f"지뢰찾기: 지뢰를 찾으세요 (남은 기회 {attempts})", True, BLACK)
        screen.blit(msg, (20, 20))

        for x in range(size):
            for y in range(size):
                rect = pygame.Rect(50+x*cell_size, 60+y*cell_size, cell_size, cell_size)
                if (x, y) in clicked_cells:
                    pygame.draw.rect(screen, RED, rect)  # 이미 선택한 칸은 빨간색
                pygame.draw.rect(screen, BLACK, rect, 1)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = event.pos
                grid_x = (pos[0]-50)//cell_size
                grid_y = (pos[1]-60)//cell_size
                if 0 <= grid_x < size and 0 <= grid_y < size:
                    if (grid_x, grid_y) == (mine_x, mine_y):
                        result = "W"
                    else:
                        clicked_cells.add((grid_x, grid_y))
                        attempts -= 1
                        if attempts <= 0:
                            result = "L"

    if result == "W":
        state = "success"
    else:
        state = "fail"

# --------------------
# 경로2: 숫자 맞히기
# --------------------
def play_number_guess():
    global state
    number = random.randint(1, 100)
    guess = None
    attempts = 3
    input_text = ""
    result = None
    message = "1~100 사이 숫자를 맞혀보세요."

    while result is None:
        screen.fill(WHITE)
        msg = font_small.render(message + f" (남은 기회 {attempts})", True, BLACK)
        msg_rect = msg.get_rect(center=(WIDTH//2, 100))
        screen.blit(msg, msg_rect)

        input_box = pygame.Rect(WIDTH//2 - 70, HEIGHT//2 - 20, 140, 40)
        pygame.draw.rect(screen, BLACK, input_box, 2)
        txt_surface = font_small.render(input_text, True, BLACK)
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and input_text.isdigit():
                    guess = int(input_text)
                    if guess == number:
                        result = "W"
                    else:
                        attempts -= 1
                        if attempts <= 0:
                            result = "L"
                        elif guess < number:
                            message = "UP!"
                        else:
                            message = "DOWN!"
                    input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    if event.unicode.isdigit():
                        input_text += event.unicode

    if result == "W":
        state = "success"
    else:
        state = "fail"

# --------------------
# 경로3: 가위바위보
# --------------------
def play_rps():
    global state
    win_count = 0
    result = None
    choices = ["가위", "바위", "보"]
    buttons = []
    for i, text in enumerate(choices):
        x = 100 + i*150
        y = 300
        surf = pygame.Surface((100, 60))
        surf.fill(GREEN)
        buttons.append(ImageButton(text, x, y, surf, None))

    while result is None:
        screen.fill(WHITE)
        msg = font_small.render(f"가위바위보: 2번 이기면 성공! 현재 승리 {win_count}", True, BLACK)
        msg_rect = msg.get_rect(center=(WIDTH//2, 100))
        screen.blit(msg, msg_rect)
        for b in buttons:
            b.draw()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = event.pos
                for b in buttons:
                    if b.rect.collidepoint(pos):
                        player = b.text
                        comp = random.choice(choices)
                        if (player == "가위" and comp == "보") or \
                           (player == "바위" and comp == "가위") or \
                           (player == "보" and comp == "바위"):
                            win_count += 1
                            if win_count >= 2:
                                result = "W"
                        else:
                            result = "L"

    if result == "W":
        state = "success"
    else:
        state = "fail"

# --------------------
# 경로 선택 함수
# --------------------
def choose_path(path_id):
    if path_id == 1:
        play_minesweeper()
    elif path_id == 2:
        play_number_guess()
    elif path_id == 3:
        play_rps()

def go_back():
    global state
    state = "menu"

# --------------------
# 버튼 생성
# --------------------
button_width, button_height = button_img.get_size()
button_spacing = 20
paths = ["경로 1: 지뢰찾기", "경로 2: 숫자 맞히기", "경로 3: 가위바위보"]
buttons_menu = []

total_height = len(paths) * button_height + (len(paths) - 1) * button_spacing
start_y = (HEIGHT - total_height) // 2

for i, path_text in enumerate(paths):
    x = (WIDTH - button_width) // 2
    y = start_y + i * (button_height + button_spacing)
    buttons_menu.append(ImageButton(path_text, x, y, button_img, lambda pid=i+1: choose_path(pid)))

# 뒤로가기 버튼
back_img = pygame.Surface((300, 60))
back_img.fill(RED)
button_back = ImageButton("뒤로가기", (WIDTH - 300)//2, start_y + total_height + 20, back_img, go_back)

# --------------------
# 게임 상태
# --------------------
state = "menu"

# --------------------
# 메인 루프
# --------------------
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = event.pos
            if state == "menu":
                for b in buttons_menu:
                    b.click(pos)
            elif state in ["fail", "success"]:
                button_back.click(pos)

    if state == "menu":
        title = font_title.render("경로를 선택하세요", True, BLACK)
        title_rect = title.get_rect(center=(WIDTH//2, start_y - 50))
        screen.blit(title, title_rect)
        for b in buttons_menu:
            b.draw()
    elif state == "success":
        msg = font_title.render("최종 성공!", True, GREEN)
        msg_rect = msg.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(msg, msg_rect)
        button_back.draw()
    elif state == "fail":
        msg = font_title.render("실패. 다시 시도하세요.", True, RED)
        msg_rect = msg.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(msg, msg_rect)
        button_back.draw()

    pygame.display.flip()

pygame.quit()
sys.exit()


