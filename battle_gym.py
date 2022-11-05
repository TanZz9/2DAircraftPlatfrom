from Box2D import *
import gym
import pygame
import numpy as mp
import math
import random
import time

# use openai gym to create a multi agent combat environmet
class battlegym(gym.Env):
    def __init__(self):
        # define the screen
        self.screen = pygame.display.set_mode((640, 480), 0, 32)
        pygame.display.set_caption('Simple pygame example')
        self.clock = pygame.time.Clock()
        # define the world
        self.world = world(gravity=(0, 0), doSleep=True)
        # define the aircraft
        self.aircraft = []
        # define the bullet
        self.bullet = []
        # define the bullet speed
        self.bullet_speed = 10
        # define the bullet damage
        self.bullet_damage = 10
        # define the aircraft speed
        self.aircraft_speed = 10
        # define the aircraft health
        self.aircraft_health = 100
        # define the aircraft damage
        self.aircraft_damage = 10
        # define the aircraft armor
        self.aircraft_armor = 10
        # define the aircraft range
        self.aircraft_range = 10
        # define the aircraft attack speed
        self.aircraft_attack_speed = 10
        # define the aircraft attack cooldown
        self.aircraft_attack_cooldown = 0
        # define the aircraft attack cooldown
        self.aircraft_attack_cooldown_max = 10
        # define the aircraft attack cooldown
        self.aircraft_attack_cooldown_min = 0
        # define the aircraft attack cooldown
        self.aircraft_attack_cooldown_step = 1
        # define the aircraft attack cooldown
        self.aircraft_attack_cooldown_reset = 0
        # define the aircraft attack cooldown
        self.aircraft_attack_cooldown_reset_max = 10
        # define the aircraft attack cooldown
        self.aircraft_attack_cooldown_reset_min = 0
        # define the aircraft attack cooldown
        self.aircraft_attack_cooldown_reset_step = 1
        # define the aircraft attack cooldown
        self.aircraft_attack_cooldown_reset_reset = 0
        # define the aircraft attack cooldown
        self.aircraft_attack_cooldown_reset_reset_max = 10
        # define the aircraft attack cooldown
        self.aircraft_attack_cooldown_reset_reset_min = 0
        # define the aircraft attack cooldown
        self.aircraft_attack_cooldown_reset_reset_step = 1
        # define the aircraft attack cooldown
        self.aircraft_attack_cooldown_reset_reset_reset = 0
        # define the aircraft attack cooldown
        self.aircraft_attack_cooldown_reset_reset_reset_max = 10
        # define the aircraft attack cooldown
        self.aircraft_attack_cooldown_reset_reset_reset_min = 0
        # define the aircraft attack cooldown

    def render(self):
        # render the screen
        pygame.display.update()
        # render the clock
        self.clock.tick(60)

    def reset(self):
        # reset the aircraft
        self.aircraft = []
        # reset the bullet
        self.bullet = []
        # reset the bullet speed
        self.bullet_speed = 10
        # reset the bullet damage
        self.bullet_damage = 10
        # reset the aircraft speed
        self.aircraft_speed = 10
        # reset the aircraft health
        self.aircraft_health = 100
        # reset the aircraft damage
        self.aircraft_damage = 10
        # reset the aircraft armor
        self.aircraft_armor = 10
        # reset the aircraft range
        self.aircraft_range = 10
        # reset the aircraft attack speed
        self.aircraft_attack_speed = 10
        # reset the aircraft attack cooldown
        self.aircraft_attack_cooldown = 0
        # reset the aircraft attack cooldown
        self.aircraft_attack_cooldown_max = 10
        # reset the aircraft attack cooldown
        self.aircraft_attack_cooldown_min = 0
        # reset the aircraft attack cooldown
        self.aircraft_attack_cooldown_step = 1
        # reset the aircraft attack cooldown
        self.aircraft_attack_cooldown_reset = 0
        # reset the aircraft attack cooldown
        self.aircraft_attack_cooldown_reset_max = 10
        # reset the aircraft attack cooldown
        self.aircraft_attack_cooldown_reset_min = 0
        # reset the aircraft attack cooldown
        self.aircraft_attack_cooldown_reset_step = 1
        # reset the aircraft attack cooldown
        self.aircraft_attack_cooldown_reset_reset = 0
        # reset the aircraft attack cooldown
        self.aircraft_attack_cooldown_reset_reset_max = 10
        # reset the aircraft attack cooldown
        self.aircraft_attack_cooldown_reset_reset_min = 0
        # reset the aircraft attack cooldown
        self.aircraft_attack_cooldown_reset_reset_step = 1
        # reset the aircraft attack cooldown
        self.aircraft_attack_cooldown_reset_reset_reset = 0
        # reset the aircraft attack cooldown
        self.aircraft_attack_cooldown_reset_reset_reset_max = 10
        # reset the aircraft attack cooldown
        self.aircraft_attack_cooldown_reset_reset_reset_min = 0
        # reset the aircraft attack cooldown
        self.aircraft_attack_cooldown_reset_reset_reset_step = 1
        # reset the aircraft attack cooldown
