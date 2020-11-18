
import pygame
import math
import random
import time
from itertools import cycle

pygame.init()
# pygame.mixer.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Boids')

# setting clock
clock = pygame.time.Clock()

# colors:
colors = cycle(((0, 255, 0), (10, 255, 0), (20, 255, 0), (30, 255, 0), (40, 255, 0), (50, 255, 0), (60, 255, 0), (70, 255, 0), (80, 255, 0), (90, 255, 0), (100, 255, 0), (110, 255, 0), (120, 255, 0), (130, 255, 0), (140, 255, 0), (150, 255, 0), (160, 255, 0), (170, 255, 0), (180, 255, 0), (190, 255, 0), (200, 255, 0), (210, 255, 
0), (220, 255, 0), (230, 255, 0), (240, 255, 0), (250, 255, 0), (255, 255, 0)))
color = next(colors)

def midpoint(p1, p2):
	# minusing 12.5 so rec will be at center
    return ((p1[0]+p2[0])/2 - 25, (p1[1]+p2[1])/2 - 25)

class gameobject():
	def __init__(self, image, angle, pcolor = 0):

		self.x = 400
		self.y = 300
		self.original_image = image
		# color_surface(self.original_image, random.choice(c))
		if pcolor != 0:
			self.color = pcolor
		else:
			self.color = color
		self.original_image = pygame.mask.from_surface(self.original_image).to_surface(setcolor = self.color, unsetcolor = (0, 0, 0, 0))
		self.rotated_image = self.original_image
		self.rect = pygame.Rect(self.x, self.y, 100, 100)
		self.image_rect = self.original_image.get_rect()
		self.angle = angle
		self.rrect = 0
		self.lrect = 0

	def updategame(self ):
		if self.y <= dy[0] or self.y >= dy[1]:
			if self.y <= dy[0]:
				self.y = dy[1]
			else:
				self.y = dy[0]
		elif self.x <= dx[0] or self.x >= dx[1]:
			if self.x <= dx[0]:
				self.x = dx[1]
			else:
				self.x = dx[0]
		self.adjustbox()
		# updating values
		width = int(self.rotated_image.get_width()/2)
		height = int(self.rotated_image.get_height()/2)

		self.rotated_image = pygame.transform.rotate(self.original_image, self.angle)
		self.image_rect.x = self.x - width
		self.image_rect.y = self.y - height
		self.rect = pygame.Rect(self.x - 50, self.y - 50, 100, 100)
		if drawrecs:
			pygame.draw.rect(screen, self.color, self.image_rect)
			# pygame.draw.rect(screen, (255, 0, 255, 0), self.lrect)
			# pygame.draw.rect(screen, (255, 0, 0, 0), self.rrect)

		# pygame.draw.rect(screen, color, self.rect)
		screen.blit(self.rotated_image, (self.x - width, self.y - height))

	def adjustbox(self ):
		center = self.rect.center
		if self.angle >= 45 and self.angle <= 135:
			self.lrect = pygame.Rect(midpoint(center, self.rect.bottomright), (50, 50))
			self.rrect = pygame.Rect(midpoint(center, self.rect.bottomleft), (50, 50))

		elif self.angle >= 225 and self.angle <= 315:
			self.lrect = pygame.Rect(midpoint(center, self.rect.topleft), (50, 50))
			self.rrect = pygame.Rect(midpoint(center, self.rect.topright), (50, 50))

		elif self.angle >= 135 and self.angle <= 225:
			self.lrect = pygame.Rect(midpoint(center, self.rect.topright), (50, 50))
			self.rrect = pygame.Rect(midpoint(center, self.rect.bottomright), (50, 50))

		elif (self.angle >= 315 and self.angle <= 360) or (self.angle >= 0 and self.angle <= 45):
			self.lrect = pygame.Rect(midpoint(center, self.rect.bottomleft), (50, 50))
			self.rrect = pygame.Rect(midpoint(center, self.rect.topleft), (50, 50))

	def rotateright(self ):
		self.angle -= 2
		self.angle %= 360 
	
	def rotateleft(self ):
		self.angle += 2
		self.angle %= 360

	def ruleone(self ):
		# boids steer away from other boids
		megarect = self.rrect.union(self.lrect)
		collidecheck = megarect.collidelistall([i for i in ready if i != self])
		if collidecheck != []:
			for i in collidecheck:
				if self.rrect.colliderect(ready[i].image_rect):
					self.rotateleft()
				elif self.lrect.colliderect(ready[i].image_rect):
					self.rotateright()
				# else:
				# 	print('nani')

	def setpos(self, diff):
		self.x += diff*(math.cos(math.radians(self.angle)))
		self.y -= diff*(math.sin(math.radians(self.angle)))



dx = (-30, 815)
dy = (-30, 615)
white = pygame.transform.scale(pygame.image.load('paper-plane.png'), (25, 25))
# white.convert_alpha()
def move(i):
	# player ship - arrow keys
	if player == i:
		i.updategame()
	else:
		i.updategame()
		i.setpos(-80*delta)
		i.ruleone()

# formatting configuration menu
def multlines(text, configs, fontsize):
	text = text.replace('True', 'ON').replace('False', 'OFF').splitlines()
	for i, j in enumerate(text):
		screen.blit(configs.render(j, True, (0, 0, 0)), (0, fontsize*i))


def update():
	# drawing backround
	if pyupdate:
		# screen.fill((30, 20, 30))
		screen.fill((255, 255, 255))
	# screen.fill(color)
	# draws  configs
	if configuration:
		multlines(text, configs, 12)

	# update player,enemy position
	for i in ready:
		move(i)
	# creates frame in window
	pygame.display.update()


configs = pygame.font.Font('freesansbold.ttf',12)




drawrecs = False
pyupdate = True
configuration = True
ready = []
recs = []
run = True
epress = True
ppress = True
configcheck = True
count = 1

ready.append(gameobject(white, angle=random.randint(0, 359)))
player = gameobject( image = white, angle = random.randint(0, 359), pcolor = (255, 0, 0))
ready.append(player)

while run:
	# returns each event in keyboard
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
			continue
		


	mx, my = pygame.mouse.get_pos()
	# updating delta value and setting frame rate
	delta = clock.tick(60)/1000
	# updating game configs 
	text = f'[F7]drawrecs: {drawrecs}\n[F8]update: {pyupdate}\n[F9]configs: {configuration}\n[\]exit\nfps: {round(clock.get_fps(), 2)}\nliveboids: {len(ready)}\nmouse: {mx, my}'
	
	# updating color
	if count % 2 == 0:
		color = next(colors)
	count += 1

	recs = [i.image_rect for i in ready]

	# controlling ships
	keys = pygame.key.get_pressed()

	# allows keypresses 1 - K12 to change game settings
	if configcheck:
		if keys[pygame.K_F7]:
			drawrecs = not drawrecs
			configcheck = False

		elif keys[pygame.K_F8]:
			pyupdate = not pyupdate
			configcheck = False

		elif keys[pygame.K_F9]:
			configuration = not configuration
			configcheck = False
	
		elif keys[pygame.K_BACKSLASH]:
			run = False
			continue

		elif keys[pygame.K_SPACE]:
			ready.append(gameobject(white, angle = random.randint(0, 359)))
			configcheck = False
	if keys[pygame.K_UP]:
		player.setpos(-80*delta)

	if keys[pygame.K_LEFT]:
		player.rotateleft()

	if keys[pygame.K_RIGHT]:
		player.rotateright()

	if keys[pygame.K_DOWN]:
		player.setpos(80*delta)

	# activate on release
	if event.type == pygame.KEYUP:
		if event.key == pygame.K_LSHIFT:
			ppress = True
			configcheck = True
		elif configcheck == False and event.key in [pygame.K_F7, pygame.K_F8, pygame.K_F9, pygame.K_BACKSLASH, pygame.K_SPACE]:
			configcheck = True

	update()






