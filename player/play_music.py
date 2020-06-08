import pygame
import pygame 

file = "D:\python_core\song\I_am_a_rider-lamborghini(256k).mp3"
pygame.init()
pygame.display.set_mode((200, 100))
pygame.mixer.music.load(file)
pygame.mixer.music.play(0)

clock = pygame.time.Clock()
clock.tick(10)
while pygame.mixer.music.get_busy():
    pygame.event.poll()
    clock.tick(10)
