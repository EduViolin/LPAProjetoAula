#!/usr/bin/python
#-*- coding: utf-8 -*-
import pygame

from code.Const import KEY_UP, SCREEN_WIDTH, SCREEN_HEIGHT, KEY_RIGHT, KEY_DOWN, KEY_LEFT, ENTITY_SPEED
from code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]

        if pressed_key[KEY_DOWN[self.name]] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]

        if pressed_key[KEY_RIGHT[self.name]] and self.rect.right < SCREEN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]

        if pressed_key[KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]

    def update(self):
        self.move()
