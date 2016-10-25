import pygame
import os
from pygame.locals import *


# Module im selben Verzeichnis
import lines
import vehicles
import render
import menu
import player
import map


pygame.init()

DISPLAYSURF = pygame.display.set_mode((800, 600), DOUBLEBUF)
pygame.display.set_caption('VinVG')
pygame.mouse.set_visible(1)
pygame.key.set_repeat(1, 30)
FPSCLOCK = pygame.time.Clock()

k = map.karte("Testlevel1.map")
r = render.render(k, DISPLAYSURF)
m = menu.menü(DISPLAYSURF, r)
s = player.player()


# Hauptschleife
while True:
	DISPLAYSURF.fill((0, 0, 0))
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			os.sys.exit()
		if event.type == KEYUP:
			if event.key == K_ESCAPE:
				pygame.quit()
				os.sys.exit()
# Tastendrücke Pfeiltasten
		if event.type == KEYDOWN:
			if event.key == K_UP:
				r.scroll_up()
			if event.key == K_DOWN:
				r.scroll_down()
			if event.key == K_LEFT:
				r.scroll_left()
			if event.key == K_RIGHT:
				r.scroll_right()

# Maus
		if event.type == MOUSEBUTTONUP:
			pos = pygame.mouse.get_pos()
			# Wenn Click im Menübereich
			if(pos[1] >= m.get_Versatz_Y()):
				for button in m.get_Buttons():
					if button.collidepoint(pos) == True:
						print(button.get_name())
						button.run()
			# Wenn Click oberhalb des Menübereiches
			else:
				print("Click at " + str(k.cart2iso(pos)))


	r.hintergrund()					# Hintergrund malen
	r.vordergrund()					# Vordergrund = Gebäude malen
	r.fahrzeuge()					# Fahrzeuge malen
	m.menü() 						# Menü
	pygame.display.update()
	FPSCLOCK.tick(30) 				# Frames pro Sekunde (FPS)
