#Lập trình game Magic Roll
import random
import pygame
import sys
from objects import Balls, Coins, Tiles, Particle, Message, Button

#Phần khởi tạo của pygame, cài đặt kích thước và chế độ hiển thị cửa sổ trò chơi
pygame.init() 
SCREEN = WIDTH, HEIGHT = 350, 550
CENTER = WIDTH // 2, HEIGHT // 2 # tính toạ độ trung tâm của màn hình 
info = pygame.display.Info()  #lấy thông tin về màn hình hiển thị của hệ thống

win = pygame.display.set_mode(SCREEN, pygame.NOFRAME)

pygame.display.set_caption('Magic roll') #Tiêu đề cửa sổ game

# Cài FPS = 95 (Khung hình trên mỗi giây)
clock = pygame.time.Clock() #kiểm soát tốc độ khung hình
FPS = 95

#Thêm ảnh background
background_img = pygame.image.load('Assets/background.png')

# COLORS
INRED = (255, 106, 106)
GREEN = (193, 255, 193)
BLUE = (30, 144, 255)
ORANGE = (252, 76, 2)
YELLOW = (254, 221, 0)
PURPLE = (221, 160, 221)
AQUA = (0, 103, 127)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (25, 25, 25)
SKYBLUE = (176, 226, 255)
CORAL = (255, 192, 203)
ROSE = (255, 228, 225)
LAVENDER = (255, 240, 245)

color_list = [PURPLE, GREEN, INRED, ORANGE, YELLOW, SKYBLUE, CORAL, LAVENDER ]
color_index = 0
color = color_list[color_index]

# SOUNDS
flip_fx = pygame.mixer.Sound('Sounds/flip.mp3')
score_fx = pygame.mixer.Sound('Sounds/point.mp3')
dead_fx = pygame.mixer.Sound('Sounds/dead.mp3')
score_page_fx = pygame.mixer.Sound('Sounds/score_page.mp3')

# Xử lí âm thanh nền của trò chơi
pygame.mixer.music.load('Sounds/bgm.mp3')
pygame.mixer.music.play(loops=-1)
pygame.mixer.music.set_volume(0.7)

# FONTS
title_font = "Fonts/SVN-Transformer.ttf"
score_font = "Fonts/DroneflyRegular-K78LA.ttf"
game_over_font = "Fonts/ghostclan.ttf"
final_score_font = "Fonts/SVN-Zero.ttf"
new_high_font = "Fonts/SVN-Neogrey.ttf"

# Sử dụng font chữ khác nhau cho các đối tượng văn bản
connected = Message(WIDTH//2, 100, 45, "Magic roll", title_font, CORAL, win) 
# Đối tượng connected hiển thị ở cửa sổ win với chiều ngang = WIDTH/2, cao 100, kích thước 45
score_msg = Message(WIDTH//2, 90, 60, "0", score_font, (255, 228, 225), win)
game_msg = Message(110, 130, 40, "GAME", game_over_font, SKYBLUE, win)
over_msg = Message(240, 130, 40, "OVER!", game_over_font, WHITE, win)
final_score = Message(WIDTH//2, HEIGHT//2-20, 70, "0", final_score_font, INRED, win)
new_high_msg = Message(WIDTH//2, HEIGHT//2+80, 20,
                       "Thành tích mới", new_high_font, GREEN, win)

# Thêm ảnh các nút nhấn trong game
home_img = pygame.image.load('Assets/homeBtn.png')
replay_img = pygame.image.load('Assets/replay.png')
sound_off_img = pygame.image.load("Assets/soundOffBtn.png")
sound_on_img = pygame.image.load("Assets/soundOnBtn.png")
easy_img = pygame.image.load("Assets/easy.png")
hard_img = pygame.image.load("Assets/hard.png")
exit_img = pygame.image.load("Assets/exit.png")

# Cài đặt các nút nhấn
easy_btn = Button(easy_img, (75, 50), WIDTH//4 - 10 , HEIGHT-120)
hard_btn = Button(hard_img, (75, 50), WIDTH//2 + 25 , HEIGHT-120)
home_btn = Button(home_img, (24, 24), WIDTH // 4 - 18, HEIGHT//2 + 135)
replay_btn = Button(replay_img, (36, 36), WIDTH // 2 - 18, HEIGHT//2 + 130)
sound_btn = Button(sound_on_img, (24, 24), WIDTH -
                   WIDTH // 4 - 18, HEIGHT//2 + 135)
exit_button = Button(exit_img,(30, 30),WIDTH//2 + 125, HEIGHT//2 - 255)
# Tạo các Group để dễ quản lí các đối tượng trong game
RADIUS = 90  # bán kính của hình tròn (balls)
ball_group = pygame.sprite.Group() #bóng
coin_group = pygame.sprite.Group() #đồng xu
tile_group = pygame.sprite.Group() #chướng ngại vật 
particle_group = pygame.sprite.Group() #các hạt phát ra khi bóng va chạm 

#Tạo 2 đối tượng bóng ở màn hình trò chơi
#Đặt ở phía trên đường kính của màn hình, nằm ở các góc phần tư 1 và 2 của hình tròn
# ball = Balls((CENTER[0], CENTER[1]+RADIUS), RADIUS, 90, win)
# ball_group.add(ball) #thêm đối tượng 'ball' vào nhóm 'ball_group'
#Đặt ở dưới đường kính của màn hình, ở các góc phần tư 3 và 4 của hình tròn
# ball = Balls((CENTER[0], CENTER[1]-RADIUS), RADIUS, 270, win)
# ball_group.add(ball)
def animation():
    for i in range(1,360,60):
        ball = Balls((CENTER[0], CENTER[1]-RADIUS), RADIUS, i, win)
        ball_group.add(ball)

# Cài đặt thời gian trong trò chơi
start_time = pygame.time.get_ticks() #lấy thời điểm bắt đầu chạy trò chơi
current_time = 0 #biến để theo dõi thời gian hiện tại
coin_delta = 850 #biến để xác định thời gian xuất hiện các đồng xu
tile_delta = 2000 #biến để xác định thời gian xuất hiện chướng ngại vật

# BOOL VARIABLES
clicked = False #kiểm tra xem người chơi nhấn chuột chưa
new_coin = True #biến để xác địn xem có tạo đồng xu mới hay không
num_clicks = 0 #biến lưu số lần người chơi nhấn chuột
score = 0 #biến lưu điểm số của người chơi

player_alive = True #biến để xác nhận người chơi còn sống (chưa thua)
highscore = 0 #biến lưu điểm số cao nhất 
sound_on = True #biến để xác định âm thanh trò chơi bật hay tắt
easy_level = True #biến để xác định xem trò chơi có ở mức độ dễ hay không

#các biến xác định trạng thái hiên thị của màn hình trò chơi
home_page = True
game_page = False
score_page = False

running = True
# Khi game được chạy
animation()
while running:
    # Tạo background cho game
    win.blit(background_img, (0, 0)) #vẽ background
    # Màn hình game
    pygame.draw.rect(win, PURPLE, (0, 0, WIDTH, HEIGHT), 5, border_radius=10) #Tạo màu viền cho màn hình
    clock.tick(FPS)  # Screen FPS
    exit_button.draw(win) # tạo exit button
    # Lấy các sự kiện trong hàng đợi sự kiện của pygame
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False #khi người chơi tắt cửa sổ thì trò chơi kết thúc

        # Xử lý sự kiện bàn phím khi người chơi nhấn phím.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or \
                    event.key == pygame.K_q:
                running = False 
                # Nếu người chơi nhấn phím ESCAPE hoặc "q", trò chơi kết thúc
                
        # xử lý sự kiện click chuột vào dấu X
        if event.type == pygame.MOUSEBUTTONDOWN:
                if exit_button.draw(win):  # Kiểm tra nếu chuột được nhấn vào button
                    running = False     
                     
        # Xử lí sự kiện người chơi nhấn chuột khi đang ở màn hình trò chơi đang hiển thị
        if event.type == pygame.MOUSEBUTTONDOWN and game_page:
            #Nếu sự kiện là nhấp chuột thì biến clicked=true và thực hiện thao tác sau
            if not clicked:
                clicked = True
                # lặp qua tất cả các đối tượng bóng trong "ball_group"
                for ball in ball_group:
                    ball.dtheta *= -1 #Đảo ngược hướng quay của bóng khi người chơi nhấn chuột.
                flip_fx.play() #thêm âm thanh khi bóng đổi chiều
                # thay đổi màu bóng sau 2 lần click
                num_clicks += 1
                if num_clicks % 2 == 0:
                    color_index += 1
                    if color_index > len(color_list) - 1:
                        color_index = 0

                    color = color_list[color_index]
        # clicked = False khi người chơi nhấn chuột,để khi nhấn chuột lần nữa sẽ thực hiện các hành động trên.
        if event.type == pygame.MOUSEBUTTONDOWN and game_page:
            clicked = False

    # Khi đang ở trang chủ thì cập nhật trang chủ của trò chơi.
    if home_page:
        connected.update()
        pygame.draw.circle(win, BLACK, CENTER, 105, 30) #Vẽ vòng tròn đen ở giữa màn hình game bán kính 105, độ dày 30
        ball_group.update(color)

        # Nếu mức độ Dễ được nhấn 
        if easy_btn.draw(win):
            ball_group.empty() #làm rỗng nhóm 'ball_group'
            ball = Balls((CENTER[0], CENTER[1]+RADIUS), RADIUS, 90, win) #tạo đối tượng bóng mới và quay từ góc 90 độ
            ball_group.add(ball)
            # Khi game bắt đầu, tắt các màn hình không cần thiết
            home_page = False
            game_page = True
            easy_level = True
        # Nếu mức độ Khó được nhấn
        if hard_btn.draw(win):
            ball_group.empty()
            #Tạo hai đối tượng bóng quay từ góc 90 và 270
            ball = Balls((CENTER[0], CENTER[1]+RADIUS), RADIUS, 90, win)
            ball_group.add(ball)
            ball = Balls((CENTER[0], CENTER[1]-RADIUS), RADIUS, 270, win)
            ball_group.add(ball)
            # Khi game bắt đầu, tắt các màn hình không cần thiết
            home_page = False
            game_page = True
            easy_level = False

    #Cập nhật trang điểm (score_page) khi trò chơi đã kết thúc.
    if score_page:
        game_msg.update()  # GAME
        over_msg.update()  # OVER

        # hiển thị điểm số của người chơi khi biến score có giá trị
        if score != -1:
            final_score.update(score, color)
        # Cập nhật lại điểm số cao nhất nếu 
        if score and (score >= highscore):
            new_high_msg.update(shadow=False)

        # Nếu nút home được nhấn:
        if home_btn.draw(win):
            home_page = True #trở lại màn hình home
            score_page = False
            game_page = False
            player_alive = True
            score = 0
            score_msg = Message(WIDTH//2, 100, 60, "0",
                                score_font, (255, 228, 225), win) #hiển thị lại điểm số ban đâù là 0
            animation()
        # Nếu nút replay được nhấn:
        if replay_btn.draw(win):
            home_page = False
            score_page = False
            game_page = True #trở lại màn hình game
            score = 0
            score_msg = Message(WIDTH//2, 100, 60, "0",
                                score_font, (255, 228, 225), win) #hiển thị lại điểm số ban đâù là 0
            
            # Khi người chơi chọn chế dộ khó hoặc dễ
            if easy_level: #tạo 1 bóng ở chế độ dễ
                ball = Balls((CENTER[0], CENTER[1]+RADIUS), RADIUS, 90, win)
                ball_group.add(ball)
            else: #tạo hai bóng ở chế độ khó
                ball = Balls((CENTER[0], CENTER[1]+RADIUS), RADIUS, 90, win)
                ball_group.add(ball)
                ball = Balls((CENTER[0], CENTER[1]-RADIUS), RADIUS, 270, win)
                ball_group.add(ball)

            player_alive = True

        # Xử lí việc bật/tắt âm thanh
        if sound_btn.draw(win):
            sound_on = not sound_on
            # Update hình ảnh nút âm thanh
            if sound_on:
                sound_btn.update_image(sound_on_img)
                pygame.mixer.music.play(loops=-1)
            else:
                sound_btn.update_image(sound_off_img)
                pygame.mixer.music.stop()

    # Khi người chơi đang ở màn hình game
    if game_page:
        pygame.draw.circle(win, BLACK, CENTER, 105, 30)
        ball_group.update(color)
        coin_group.update(color)
        tile_group.update()
        score_msg.update(score)
        particle_group.update()

        # Nếu người chơi còn sống thì chướng ngại vật và đồng xu sẽ bắt đầu chuyển động 
        if player_alive: 
            for ball in ball_group:
                # sử dụng hàm pygame.sprite.spritecollide() để kiểm tra va chạm và loại bỏ đồng xu sau khi va chạm xảy ra
                if pygame.sprite.spritecollide(ball, coin_group, True): 
                    score_fx.play() #thêm âm thanh điểm số
                    score += 1 #tăng điểm số

                    # Cập nhật điểm số
                    if highscore <= score:
                        highscore = score

                    # tạo ra các hạt phát ra (particle) từ trung tâm bóng khi chạm một đồng xu.
                    x, y = ball.rect.center
                    for i in range(20): #vòng lặp để tạo 10 hạt phát ra từ quả bóng.
                        particle = Particle(x, y, color, win)
                        particle_group.add(particle) #Thêm đối tượng hạt phát ra vào nhóm particle_group.

                # Nếu người chơi va chạm với chướng ngại vật
                if pygame.sprite.spritecollide(ball, tile_group, True):
                    x, y = ball.rect.center
                    for i in range(35):
                        particle = Particle(x, y, color, win)
                        particle_group.add(particle)

                    player_alive = False #người chơi thua cuộc
                    dead_fx.play()

            # tính thời gian đã trôi qua
            current_time = pygame.time.get_ticks() #lấy thời gian hiện tại
            delta = current_time - start_time #thời gian đã trôi qua

            # Tạo ra các đồng xu 
            if coin_delta < delta < coin_delta + 100 and new_coin: #xác định khoảng thời gian đồng xu được tạo ra.
                y = random.randint(CENTER[1]-RADIUS, CENTER[1]+RADIUS) #xác định vị trí trên trục y của đồng xu.
                coin = Coins(y, win) #Tạo một đối tượng đồng xu (coin) với vị trí y 
                coin_group.add(coin)
                new_coin = False #đảm bảo rằng hiện chỉ có một đồng xu được tạo ra trên 1 trục
                
            # Tạo ra các chướng ngại 
            if delta >= tile_delta: 
                y = random.choice([CENTER[1]-80, CENTER[1], CENTER[1]+80]) # random tọa độ y
                type_ = random.randint(1, 3) # randon loại của gạch
                t = Tiles(y, type_, win) #tạo chướng ngại
                tile_group.add(t)
                new_coin = True
                start_time = current_time
        # Khi người chơi thua cuộc
        if not player_alive and len(particle_group) == 0:
            score_page = True
            game_page = False

            score_page_fx.play()

            ball_group.empty()
            tile_group.empty()
            coin_group.empty()

    
    pygame.display.update()  # updates display
# Thoát khỏi màn hình game
pygame.quit()
sys.exit()
