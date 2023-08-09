#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface


class Menu:
    def __init__(self, screen):
        self.screen: Surface = screen
        self.suf = pygame.image.load('./asset/MenuBG.png')
        self.rect = self.suf.get_rect(left=0, top=0)

    def run(self, ):
        while True:
            self.screen.blit(source=self.suf,dest=self.rect)
            pygame.display.flip()
        pass
