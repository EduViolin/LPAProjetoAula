#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.surface import Surface
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, screen, name, menu_option):
        self.screen_surface: Surface = screen
        self.name = name
        self.mode = menu_option  # Game mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('level1_BG'))

    def run(self, ):
        while True:
            for ent in self.entity_list:
                self.screen_surface.blit(source=ent.surface, dest=ent.rect)
                ent.move()
            pygame.display.flip()

        pass
