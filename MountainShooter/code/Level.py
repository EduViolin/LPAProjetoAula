import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WHITE_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT, MENU_OPTION, EVENT_ENEMY
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:
    def __init__(self, screen, name, menu_option):
        self.screen: Surface = screen
        self.name = name
        self.mode = menu_option  # Game mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('level1_BG'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        if menu_option in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY, 4000)

    def run(self):
        pygame.mixer_music.load(f'./asset/{self.name}.mp3')
        pygame.mixer_music.set_volume(0.2)
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.screen.blit(source=ent.surface, dest=ent.rect)  # desenhando minhas entidades
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
            # desenhando textos
            self.level_text(14, f'fps: {clock.get_fps() :.0f}', WHITE_COLOR, (SCREEN_WIDTH, SCREEN_HEIGHT - 1))
            self.level_text(14, f'Entity list: {len(self.entity_list)}', WHITE_COLOR, (125, SCREEN_HEIGHT - 1))
            # Atualizar a Tela
            pygame.display.flip()
            # Verificar relacionamentos entre Entidades
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
            # Conferir eventos
            for event in pygame.event.get():  # Evento sair
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(right=text_pos[0], bottom=text_pos[1])
        self.screen.blit(source=text_surf, dest=text_rect)
