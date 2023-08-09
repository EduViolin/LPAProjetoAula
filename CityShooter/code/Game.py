#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import SCREEN_WIDTH, SCREEN_HEIGHT
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    def run(self):
        pygame.mixer_music.load('./asset/Menu.wav')
        pygame.mixer_music.play(-1)

        while True:
            menu = Menu(self.screen)
            menu.run()
            pass
