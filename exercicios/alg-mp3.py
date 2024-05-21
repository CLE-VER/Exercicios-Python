import pygame

pygame.init()
pygame.mixer.music.load('W de Evellyn.mp3')
pygame.mixer.music.play()
input()

pygame.event.wait()
# Para esse cod funcionar, vai ter que instalar a biblioteca 'pygame'