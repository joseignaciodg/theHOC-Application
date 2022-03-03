#from playsound import playsound
from random import seed, random, randint
import pygame

value = randint(0, 4)
print(value)

library = ["song1.mp3","song2.mp3","song3.mp3","song4.mp3","song5.mp3"]
song = library[value]

print (song)
pygame.mixer.init()
pygame.mixer.music.load(song)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
     continue

#playsound(song)

