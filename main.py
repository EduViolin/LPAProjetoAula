import pygame
from pygame import Surface, Rect

screen_width = 576
screen_height = 324

# setup pygame module
pygame.init()
print('Setup start')
# Criando Janela no pygame
screen: Surface = pygame.display.set_mode(size=(screen_width, screen_height))

# carregando uma imagem e gerando uma superfície
bg_surface = pygame.image.load('./asset/bg.png').convert_alpha()
player1_surface = pygame.image.load('./asset/player1.png').convert_alpha()

# obter o retângulo da superfície
bg_rect: Rect = bg_surface.get_rect(left=0, top=0)
player1_rect: Rect = player1_surface.get_rect(left=50, top=170)

# Desenhar na janela(screen)
screen.blit(source=bg_surface, dest=(bg_rect))
screen.blit(source=player1_surface, dest=(player1_rect))

# atualizar a janela
pygame.display.flip()

# Colocando um relógio no game
clock = pygame.time.Clock()

# Carregar e tocar som
pygame.mixer_music.load('./asset/phase1.wav')
pygame.mixer_music.play(-1)
pygame.mixer_music.set_volume(0.4)
print('Setup end')

print('Loop start')
while True:
    clock.tick(120)  # Define o fps do game
    # print(f'{clock.get_fps():.0f}')  # Monitorar o fps
    screen.blit(source=bg_surface, dest=(bg_rect))
    screen.blit(source=player1_surface, dest=(player1_rect))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Loop end')
            pygame.quit()
            quit()
    pressed_key = pygame.key.get_pressed()
    if pressed_key[pygame.K_w] or pressed_key[pygame.K_UP]:
        player1_rect.centery -= 1
    if pressed_key[pygame.K_s] or pressed_key[pygame.K_DOWN]:
        player1_rect.centery += 1
    if pressed_key[pygame.K_d] or pressed_key[pygame.K_RIGHT]:
        player1_rect.centerx += 1
    if pressed_key[pygame.K_a] or pressed_key[pygame.K_LEFT]:
        player1_rect.centerx -= 1
