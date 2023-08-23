#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame.image
from pygame import Rect, Surface
from pygame.font import Font

from code.Const import SCREEN_WIDTH, TEXT_COLOR_MENU, MENU_OPTION, WHITE_COLOR, YELLOW_COLOR

class Menu:
    def __init__(self, screen):
        self.screen: Surface = screen
        self.suf = pygame.image.load('./asset/MenuBG.png').convert_alpha()
        self.rect = self.suf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./asset/Menu.wav')
        pygame.mixer_music.play(-1)
        menu_option = 0

        while True:
            self.screen.blit(source=self.suf, dest=self.rect)
            self.menu_text(50, "Mountain", TEXT_COLOR_MENU, ((SCREEN_WIDTH / 2), 80))
            self.menu_text(50, "Shooter", TEXT_COLOR_MENU, ((SCREEN_WIDTH / 2), 150))

            # Gerar tela
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], YELLOW_COLOR, ((SCREEN_WIDTH / 2), 200 + 30 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], WHITE_COLOR, ((SCREEN_WIDTH / 2), 200 + 30 * i))
            pygame.display.flip()

            # Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_position: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_position)
        self.screen.blit(source=text_surf, dest=text_rect)
