#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import SCREEN_WIDTH, SCREEN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'level1_BG':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'level1_BG{i}', position))
                    list_bg.append(Background(f'level1_BG{i}', (SCREEN_WIDTH, 0)))
                return list_bg

            case 'Player1':
                return Player('Player1', (10, SCREEN_HEIGHT / 2 - 20))

            case 'Player2':
                return Player('Player2', (10, SCREEN_HEIGHT / 2 + 20))

            case 'Enemy1':
                return Enemy('Enemy1', (SCREEN_WIDTH + 10, random.randint(40, SCREEN_HEIGHT-40)))

            case 'Enemy2':
                return Enemy('Enemy2', (SCREEN_WIDTH + 10, random.randint(40, SCREEN_HEIGHT-40)))
