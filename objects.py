import pygame
import random
import math

SCREEN = WIDTH, HEIGHT = 350, 550
CENTER = WIDTH // 2, HEIGHT // 2

pygame.font.init()
pygame.mixer.init()

# Tạo lớp "Balls" để biểu diễn các đối tượng bóng trong game 
# pygame.sprite.Sprite là lớp trong thư viện pygame, tạo các đối tượng có thể tham gia các hoạt động như va chạm, di chuyển,..(sprite)
class Balls(pygame.sprite.Sprite): 
    def __init__(self, pos, radius, angle, win):
        #self là tham chiếu đến đối tượng Balls hiện tại.
        super(Balls, self).__init__()
        #super() được sử dụng để gọi các phương thức và thuộc tính của lớp cha từ lớp con
        self.initial_pos = pos #Lưu trữ vị trí ban đầu của quả bóng.
        self.radius = radius #Lưu trữ bán kính của quả bóng
        self.initial_angle = angle #Lưu trữ bán kính của quả bóng
        self.win = win #Lưu trữ cửa sổ Pygame trên đó bóng sẽ được vẽ.
        self.reset() #đặt lại các thuộc tính của quả bóng.
        #Tạo quả bóng
        self.rect = pygame.draw.circle(
            self.win, (25, 25, 25), (self.x, self.y), 6)
    # cập nhật trạng thái của quả bóng
    def update(self, color):
        #x và y là tọa độ mới của quả bóng (sử dụng hàm toán học)
        x = round(CENTER[0] + self.radius *
                  math.cos(self.angle * math.pi / 180))
        y = round(CENTER[1] + self.radius *
                  math.sin(self.angle * math.pi / 180))

        self.angle += self.dtheta

        self.step += 1 #đếm số lần cập nhật vị trí của quả bóng
        if self.step % 5 == 0:
            self.pos_list.append((x, y))
            #Danh sách lưu trữ các tọa độ của quả bóng trong một khoảng thời gian
        if len(self.pos_list) > 5:
            self.pos_list.pop(0) #Loại bỏ tọa độ đầu tiên trong danh sách self.pos_list

        #tạo hiệu ứng 3D cho quả bóng.
        pygame.draw.circle(self.win, (255, 255, 255), (x, y), 7)
        #quản lý vị trí và va chạm của quả bóng
        self.rect = pygame.draw.circle(self.win, color, (x, y), 6)

        #vẽ hiệu ứng theo sau khi quả bóng di chuyển
        for index, pos in enumerate(self.pos_list): # ds lưu trữ các tọa độ của các dấu vết của quả bóng.
            #index ưu trữ chỉ số của dấu vết hiện tại
            #pos lưu trữ tọa độ của dấu vết hiện tại.
            if index < 3: 
                radius = 2 
            else:
                radius = 4
            pygame.draw.circle(self.win, color, pos, radius)

    # thiết lập lại các thuộc tính của bóng về trạng thái ban đầu.
    def reset(self):
        # thiết lập lại tọa độ x và y của bóng bằng giá trị tọa độ ban đầu 
        self.x, self.y = self.initial_pos
        # thiết lập lại góc quay của bóng bằng giá trị góc ban đầu
        self.angle = self.initial_angle 
        self.dtheta = -2
            #bóng sẽ quay theo hướng ngược chiều kim đồng hồ khi được khởi động lại.
        self.pos_list = [] #đặt lại thành ds trống khi bóng được khởi động lại
        self.step = 0

# Lớp Coins đại diện cho đồng xu trong game. 
class Coins(pygame.sprite.Sprite):
    def __init__(self, y, win): #self tham chiếu đến đối tượng Coins hiện tại
        super(Coins, self).__init__() #lấy thuộc tính, phương thức từ lớp cha cho lớp con

        self.y = y # tọa độ y của đồng xu trên màn hình.
        self.win = win
        self.size = 15 # Kích thước của đồng xu

        self.x = WIDTH + 20 # tọa độ x ban đầu của đồng xu. (ngoài màn hình bên phải)
        self.dx = -1 # tốc độ di chuyển ngang của đồng xu. 
                     # với giá trị -1, đồng xu sẽ di chuyển sang bên trái màn hình.
        self.s = 1
        # tạo đồng xu trên màn hình
        self.rect = pygame.draw.rect(
            self.win, (255, 255, 255), (self.x, self.y, self.size, self.size))

    # cập nhật vị trí và trạng thái của đồng xu trong trò chơi    
    def update(self, color):
        self.x += self.dx #cập nhật tọa độ x của đồng xu (di chuyển sang trái)
        # Nếu đồng xu đã di chuyển ra khỏi màn hình bên trái (self.x < -20) thì loại bỏ khỏi game 
        if self.x < -20:
            self.kill()

        #vẽ một hình chữ nhật trắng nhỏ bên ngoài đồng xu để tạo hiệu ứng.
        pygame.draw.rect(self.win, (200, 200, 200),
                         (self.x+self.s, self.y+self.s, self.size, self.size))
        #vẽ hình chữ nhật đại diện cho đồng xu trên màn hình
        self.rect = pygame.draw.rect(
            self.win, color, (self.x, self.y, self.size, self.size))
        #vẽ một vòng tròn nhỏ màu trắng tại trung tâm đông xu
        pygame.draw.circle(self.win, (255, 255, 255), self.rect.center, 2)

# Định nghĩa các chướng ngại vật (tiles) trong trò chơi
class Tiles(pygame.sprite.Sprite):
    def __init__(self, y, type_, win): 
        super(Tiles, self).__init__()

        self.x = WIDTH+10 # tọa độ x ban đầu của gạch ở ngoài cùng bên phải màn hình.
        self.y = y #Lưu trữ tọa độ y dưới dạng tham số đầu vào.
        self.type = type_ #Lưu trữ loại của gạch dưới dạng tham số đầu vào
        self.win = win

        # Khởi tạo các thuộc tính liên quan đến sự di chuyển và quay của gạch
        self.angle = 0
        self.dtheta = 0
        self.dx = -1

        if self.type == 1: # loại 1 có kích thước 50x20
            width = 50
            height = 20
        elif self.type == 2: # loại 2 có kích thước 20x50
            width = 20
            height = 50
        elif self.type == 3: # loại 3 kích thước 50x20 nhưng với tốc độ quay khác biệt
            width = 50
            height = 20
            self.dtheta = 2

        #Tạo một bề mặt Pygame để vẽ hình dạng và màu sắc của gạch
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.rect(self.image, (255, 255, 255),
                         (0, 0, width, height), border_radius=8) #tạo góc bo tròn cho gạch
        self.rect = self.image.get_rect(center=(self.x, self.y))

    # Xoay gạch 
    def rotate(self):
        image = pygame.transform.rotozoom(self.image, self.angle, 1)
        # xoay hình ảnh self.image một góc self.angle và không thay đổi tỷ lệ.
        rect = image.get_rect(center=self.rect.center)

        return image, rect
    
    # Cập nhật sự di chuyển của gạch trên màn hình
    def update(self):
        self.rect.x += self.dx #di chuyển sang bên trái bằng cách thay đổi tọa độ x
        if self.rect.right < 0: #Nếu phần bên phải của gạch ra khỏi biên bên trái của màn hình 
            self.kill() #thì gạch bị xóa khỏi trò chơi

        self.angle += self.dtheta # tạo hiệu ứng quay cho đối tượng gạch.
        image, self.rect = self.rotate() # hình ảnh image và hình chữ nhật self.rect sau khi xoay.

        self.win.blit(image, self.rect)

# Lớp đại diện cho các hạt nhỏ được tạo ra khi quả bóng va chạm với các viên gạch.
class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y, color, win):
        super(Particle, self).__init__()
        self.x = x
        self.y = y # Tọa độ x và y của hạt.
        self.color = color
        self.win = win
        self.size = random.randint(4, 7)
        # Kích thước ban đầu của hạt, được chọn ngẫu nhiên trong khoảng từ 4 đến 7.
        
        xr = (-3, 3)
        yr = (-3, 3)
        # Khoảng cách tối đa mà hạt có thể di chuyển theo phương x và y sau mỗi khung hình.
        f = 2 #Hệ số tốc độ
        self.life = 40 # thời gian hạt có thể tồn tại
        #Thiết lập tốc độ di chuyển của hạt
        self.x_vel = random.randrange(xr[0], xr[1]) * f
        self.y_vel = random.randrange(yr[0], yr[1]) * f
        self.lifetime = 0 #thời gian tồn tại hạt
    # cập nhật vị trí và kích thước của hạt
    def update(self):
        self.size -= 0.1 # Kích thước của hạt giảm đi 0.1 trong mỗi khung hình.
        self.lifetime += 1 #Thời gian tồn tại của hạt tăng lên 1 trong mỗi khung hình.
        if self.lifetime <= self.life: #nếu hạt vẫn trong thời gian tồn tại
            self.x += self.x_vel
            self.y += self.y_vel
            # hạt tiếp tục di chuyển bằng cách cập nhật tọa độ
            s = int(self.size)
            pygame.draw.rect(self.win, self.color, (self.x, self.y, s, s))
        else:
            self.kill() #nếu không thì loại bỏ hạt ra khỏi màn hình

# Tạo ra các thông điệp văn bản trong trò chơi.
class Message:
    def __init__(self, x, y, size, text, font, color, win):
        self.win = win
        self.color = color
        self.x, self.y = x, y #Tọa độ x và y của vị trí hiển thị của thông điệp trên màn hình.
        if not font: #nếu không có font chữ được chỉ định thì dùng font mặc định
            self.font = pygame.font.SysFont("Verdana", size)
            anti_alias = True
        else:
            self.font = pygame.font.Font(font, size)
            anti_alias = False

        #tạo văn bản chính và tạo bóng cho văn bản   
        self.image = self.font.render(text, anti_alias, color)
        self.rect = self.image.get_rect(center=(x, y))
        if self.color == (200, 200, 200):
            self.shadow_color = (255, 255, 255)
        else:
            self.shadow_color = (54, 69, 79)
        self.shadow = self.font.render(text, anti_alias, self.shadow_color)
        self.shadow_rect = self.image.get_rect(center=(x+2, y+2))

    # cập nhật văn bản được hiển thị trên màn hình
    def update(self, text=None, color=None, shadow=True):
        if text:
            if not color: 
                color = self.color
            self.image = self.font.render(f"{text}", False, color)
            self.rect = self.image.get_rect(center=(self.x, self.y))
            self.shadow = self.font.render(f"{text}", False, self.shadow_color)
            self.shadow_rect = self.image.get_rect(center=(self.x+2, self.y+2))
        if shadow:
            self.win.blit(self.shadow, self.shadow_rect)
        self.win.blit(self.image, self.rect)
    
        
# Tạo các nút trong trò chơi
class Button(pygame.sprite.Sprite):
    def __init__(self, img, scale, x, y):
        super(Button, self).__init__()

        self.scale = scale #tỷ lệ của hình ảnh nút
        self.image = pygame.transform.scale(img, self.scale)
            # chuyển đổi hình ảnh ban đầu (img) thành kích thước mới dựa trên tỷ lệ đã được cung cấp 
        self.rect = self.image.get_rect()  # tạo một hình chữ nhật bao quanh hình ảnh nút.
        self.rect.x = x
        self.rect.y = y 
        # đặt vị trí ban đầu của nút trên màn hình dựa trên các tọa độ x và y đã được cung cấp khi tạo nút.
        self.clicked = False #sử dụng để kiểm tra xem nút đã được nhấp vào hay chưa.
    #cập nhật hình ảnh mới của nút khi thay đổi nút trong quá trình chạy chương trình.
    def update_image(self, img):
        self.image = pygame.transform.scale(img, self.scale)

    #vẽ nút lên màn hình
    def draw(self, win):
        action = False
        pos = pygame.mouse.get_pos() #lấy tọa độ của con trỏ chuột trong trò chơi.
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                action = True
                self.clicked = True
                #người chơi đã nhấn vào nút trong frame này.

            if not pygame.mouse.get_pressed()[0]:
                self.clicked = False
                #người chơi đã thả nút chuột sau khi nhấn nó.

        win.blit(self.image, self.rect)
        #vẽ hình ảnh của nút lên màn hình tại vị trí và kích thước được xác định bởi self.rect.
        return action
        #Dòng này trả về True nếu người chơi đã nhấn vào nút trong frame này, ngược lại trả về False