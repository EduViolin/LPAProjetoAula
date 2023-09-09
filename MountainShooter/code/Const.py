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
                'Player1': 2,
                'Player1Shot': 3,
                'Player2': 3,
                'Player2Shot': 4,
                'Enemy1': 2,
                'Enemy1Shot': 5,
                'Enemy2': 1,
                'Enemy2Shot': 6,
                }

ENTITY_HEALTH = {'level1_BG0': 999,
                 'level1_BG1': 999,
                 'level1_BG2': 999,
                 'level1_BG3': 999,
                 'level1_BG4': 999,
                 'level1_BG5': 999,
                 'level1_BG6': 999,
                 'Player1': 300,
                 'Player1Shot': 1,
                 'Player2': 300,
                 'Player2Shot': 1,
                 'Enemy1': 50,
                 'Enemy1Shot': 1,
                 'Enemy2': 60,
                 'Enemy2Shot': 1,
                 }
ENTITY_DAMAGE = {'level1_BG0': 0,
                 'level1_BG1': 0,
                 'level1_BG2': 0,
                 'level1_BG3': 0,
                 'level1_BG4': 0,
                 'level1_BG5': 0,
                 'level1_BG6': 0,
                 'Player1': 1,
                 'Player1Shot': 25,
                 'Player2': 1,
                 'Player2Shot': 20,
                 'Enemy1': 1,
                 'Enemy1Shot': 20,
                 'Enemy2': 1,
                 'Enemy2Shot': 15,
                 }

ENTITY_SCORE = {'level1_BG0': 0,
                 'level1_BG1': 0,
                 'level1_BG2': 0,
                 'level1_BG3': 0,
                 'level1_BG4': 0,
                 'level1_BG5': 0,
                 'level1_BG6': 0,
                 'Player1': 0,
                 'Player1Shot': 0,
                 'Player2': 0,
                 'Player2Shot': 0,
                 'Enemy1': 100,
                 'Enemy1Shot': 0,
                 'Enemy2': 125,
                 'Enemy2Shot': 0,
                 }

ENTITY_SHOOT_DELAY = {'Player1': 20,
                      'Player2': 15,
                      'Enemy1': 30,
                      'Enemy2': 45,
                      }

# Teclas para controlar o player
KEY_UP = {'Player1': pygame.K_w, 'Player2': pygame.K_UP}
KEY_RIGHT = {'Player1': pygame.K_d, 'Player2': pygame.K_RIGHT}
KEY_DOWN = {'Player1': pygame.K_s, 'Player2': pygame.K_DOWN}
KEY_LEFT = {'Player1': pygame.K_a, 'Player2': pygame.K_LEFT}
KEY_SHOT = {'Player1': pygame.K_LCTRL, 'Player2': pygame.K_RCTRL}
