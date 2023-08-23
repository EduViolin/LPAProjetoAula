import pygame

SCREEN_WIDTH = 576  # largura da janela
SCREEN_HEIGHT = 324  # Altura da Janela

EVENT_ENEMY = pygame.USEREVENT + 1

TEXT_COLOR_MENU = (69, 55, 8)  # cor do texto do menu
WHITE_COLOR = (255, 255, 255)
YELLOW_COLOR = (255, 255, 128)

MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'EXIT')

ENTITY_SPEED = {'level1_BG0': 0,
                'level1_BG1': 1,
                'level1_BG2': 2,
                'level1_BG3': 3,
                'level1_BG4': 4,
                'level1_BG5': 5,
                'level1_BG6': 6,
                'Player1': 3,
                'Player2': 3,
                'Enemy1': 2,
                'Enemy2': 1}

# Teclas para controlar o player
KEY_UP = {'Player1': pygame.K_w, 'Player2': pygame.K_UP}
KEY_RIGHT = {'Player1': pygame.K_d, 'Player2': pygame.K_RIGHT}
KEY_DOWN = {'Player1': pygame.K_s, 'Player2': pygame.K_DOWN}
KEY_LEFT = {'Player1': pygame.K_a, 'Player2': pygame.K_LEFT}
KEY_SHOT = {'Player1': pygame.K_LCTRL, 'Player2': pygame.K_RCTRL}
