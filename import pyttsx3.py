"""import pyttsx3
engine = pyttsx3.init()
engine.say("hello how are u")
engine.runAndWait()"""
"""import pygame
pygame.init(); screen = pygame.display.set_mode((400, 300)); pygame.draw.circle(screen, (255, 0, 0), (200, 150), 50); pygame.display.update()"""
 
import pygame, time
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.draw.circle(screen, (255, 0, 0), (200, 150), 50)
pygame.display.update()
time.sleep(300)  # Keeps the window open for 5 minutes
pygame.quit()

"""word = "amazing" 
word[1: 6: 2]
print(word[1: 6:2])"""
