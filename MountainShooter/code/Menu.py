#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import SCREEN_WIDTH


class Menu:
    def __init__(self, screen):
        self.screen: Surface = screen
        self.suf = pygame.image.load('./asset/MenuBG.png')
        self.rect = self.suf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./asset/Menu.wav')
        pygame.mixer_music.play(-1)

        while True:
            self.screen.blit(source=self.suf, dest=self.rect)
            self.menu_text(50, "Mountain", (235, 111, 5), ((SCREEN_WIDTH / 2), 80))
            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_position: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_position)
        self.screen.blit(source=text_surf, dest=text_rect)
