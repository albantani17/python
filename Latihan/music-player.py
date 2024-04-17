import os
import pygame

def findsong(dir):
    song = [os.path.join(root, file) for root, dirs,files in os.walk(dir) for file in files if file.endswith(".mp3")]
    return song

def play(playlist):
    pygame.mixer.init()

pygame