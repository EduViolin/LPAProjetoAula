#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image

from code.Const import ENTITY_SPEED, ENTITY_HEALTH


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surface = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        self.rect = self.surface.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.mov_delay = ENTITY_SPEED[name]
        self.health = ENTITY_HEALTH[self.name]

    @abstractmethod
    def move(self):
        pass
