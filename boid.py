import pygame
import math
import random
import time
from itertools import cycle
from tkinter import *
root = Tk()
root.geometry('200x500')
root.configure(bg='black')
root.title('configs')
bs = 0
angle_diff = 60


# turn bias

# avoid bias
bavoid = .33

# follow bias
bfollow = .33

# cohesion bias
bcohes = .33


# randomize bias
def rando_bias():
	global bavoid, bfollow, bcohes
	bavoid = round(random.random(), 2)
	bfollow = round(random.randrange(0, int(100*(1 - bavoid)))/100, 2)
	bcohes =  round(1 - bavoid - bfollow, 2)
	btext.set(f'bavoid : {str(bavoid)}\nbfollow : {str(bfollow)}\nbcohes : {str(bcohes)}')




text1 = StringVar()
def incspd():
	global bs
	bs += 10
	text1.set(bs)
def decspd():
	global bs
	bs -= 10
	text1.set(bs)

text2 = StringVar()
def incangle():
	global angle_diff
	angle_diff += 10
	text2.set(angle_diff)
def decangle():
	global angle_diff
	angle_diff -= 10
	text2.set(angle_diff)

def add5():
	for i in range(5) : ready.append(gameobject(white, angle = random.randint(0, 359)))

def rem5():
	for i in range(5) : ready.pop()


text1.set(bs)
button = Button(root,text = 'Inc speed', command = incspd)
button.grid(row = 0, column = 0, sticky = W + E + N + S)
button1 = Button(root, text='Dec speed', command = decspd)
button1.grid(row = 0, column= 1, sticky = W + E + N + S)
textbox1 = Label(root, textvariable = text1)
textbox1.grid(row = 0, column = 2, sticky = W + E + N + S)

text2.set(angle_diff)
button3 = Button(root,text = 'Inc angle', command = incangle)
button3.grid(row = 1, column = 0, sticky = W + E + N + S)
button4 = Button(root,text = 'Dec angle', command = decangle)
button4.grid(row = 1, column = 1, sticky = W + E + N + S)
textbox3 = Label(root, textvariable = text2)
textbox3.grid(row = 1, column = 2, sticky = W + E + N + S)

btext = StringVar()
btext.set(f'bavoid : {str(bavoid)}\nbfollow : {str(bfollow)}\nbcohes : {str(bcohes)}')
button2 = Button(root,text = 'randomize bias', command = rando_bias)
button2.grid(row = 2, column = 0, sticky = W + E + N + S)
textbox2 = Label(root, textvariable = btext)
textbox2.grid(row = 2, column = 1, columnspan = 3, sticky = W + E + N + S)

button6 = Button(root,text = 'add 5 boids', command = add5)
button6.grid(row = 3, column = 0, sticky = W + E + N + S)

button6 = Button(root,text = 'remove 5 boids', command = rem5)
button6.grid(row = 3, column = 1, sticky = W + E + N + S)






pygame.init()
# pygame.mixer.init()

screen=pygame.display.set_mode((800, 600))
screen=pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption('Boids')

# setting clock
clock=pygame.time.Clock()

# colors:
colors = cycle(((0, 255, 0), (10, 255, 0), (20, 255, 0), (30, 255, 0), (40, 255, 0), (50, 255, 0), (60, 255, 0), (70, 255, 0), (80, 255, 0), (90, 255, 0), (100, 255, 0), (110, 255, 0), (120, 255, 0), (130, 255, 0), (140, 255, 0), (150, 255, 0), (160, 255, 0), (170, 255, 0), (180, 255, 0), (190, 255, 0), (200, 255, 0), (210, 255,
0), (220, 255, 0), (230, 255, 0), (240, 255, 0), (250, 255, 0), (255, 255, 0)))
color=next(colors)


def midpoint(p1, p2):
	return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)

def midpoint_1(p1, p2):
	return ((p1[0]+p2[0])/2 - 25, (p1[1]+p2[1])/2 - 50)

def midpoint_2(p1, p2):
	return ((p1[0]+p2[0])/2 - 50, (p1[1]+p2[1])/2 - 25)

def avgpoint(listx, listy, length):
	return sum(listx)/length, sum(listy)/length

class gameobject():
	def __init__(self, image, angle, pcolor=0):

		self.x=400
		self.y=300
		self.original_image=image
		self.color1=(255, 0, 0)
		self.color2=(255, 0, 0)
		if pcolor != 0:
			self.color=pcolor
		else:
			self.color = color
		self.original_image = pygame.mask.from_surface(self.original_image).to_surface(setcolor = self.color, unsetcolor = (0, 0, 0, 0))
		self.rotated_image = self.original_image
		self.rect = pygame.Rect(self.x, self.y, 100, 100)
		self.image_rect = self.original_image.get_rect()
		self.angle = angle
		self.dontskiprule123 = True
		self.rrect = 0
		self.lrect = 0
		self.left = False
		self.right = False
		self.vision=0

	def updategame(self):
		if self.y <= dy[0] or self.y >= dy[1]:
			if self.y <= dy[0]:
				self.y=dy[1]
			else:
				self.y=dy[0]
		elif self.x <= dx[0] or self.x >= dx[1]:
			if self.x <= dx[0]:
				self.x=dx[1]
			else:
				self.x=dx[0]

		self.adjustbox()

		# updating values
		width=int(self.rotated_image.get_width()/2)
		height=int(self.rotated_image.get_height()/2)

		self.angle %= 360
		self.rotated_image=pygame.transform.rotate(self.original_image, self.angle)
		self.image_rect.x=self.x - width
		self.image_rect.y=self.y - height
		self.rect=pygame.Rect(self.x - 50, self.y - 50, 100, 100)

		if drawrecs:
			# pygame.draw.rect(screen, self.color, self.image_rect)
			# pygame.draw.rect(screen, self.color1, self.lrect)
			# pygame.draw.rect(screen, self.color2, self.rrect)
			pygame.draw.rect(screen, (0, 80, 0, 100), self.vision)
			pygame.draw.rect(screen, (0, 200, 0, 100), self.image_rect)

		screen.blit(self.rotated_image, (self.x - width, self.y - height))

	def adjustbox(self ):
		center=self.rect.center
		if self.angle >= 45 and self.angle <= 135:
			# bottom
			# self.lrect = pygame.Rect(midpoint(center, self.rect.bottomright), (50, 50))
			# self.rrect = pygame.Rect(midpoint(center, self.rect.bottomleft), (50, 50))
			self.lrect=pygame.Rect(midpoint_1(center, self.rect.midright), (50, 100))
			self.rrect=pygame.Rect(midpoint_1(center, self.rect.midleft), (50, 100))
			self.vision=pygame.Rect(midpoint(self.rect.topleft, self.rect.midleft), (100, 75))

		elif self.angle >= 225 and self.angle <= 315:
			# top
			# self.lrect = pygame.Rect(midpoint(center, self.rect.topleft), (50, 50))
			# self.rrect = pygame.Rect(midpoint(center, self.rect.topright), (50, 50))
			self.lrect=pygame.Rect(midpoint_1(center, self.rect.midleft), (50, 100))
			self.rrect=pygame.Rect(midpoint_1(center, self.rect.midright), (50, 100))
			self.vision=pygame.Rect(self.rect.topleft, (100, 75))

		elif self.angle >= 135 and self.angle <= 225:
			# right
			# self.lrect = pygame.Rect(midpoint(center, self.rect.topright), (50, 50))
			# self.rrect = pygame.Rect(midpoint(center, self.rect.bottomright), (50, 50))
			self.lrect=pygame.Rect(midpoint_2(center, self.rect.midtop), (100, 50))
			self.rrect=pygame.Rect(midpoint_2(center, self.rect.midbottom), (100, 50))
			self.vision=pygame.Rect(midpoint(self.rect.topleft, self.rect.midtop), (75, 100))

		elif (self.angle >= 315 and self.angle <= 360) or (self.angle >= 0 and self.angle <= 45):
			# left
			# self.lrect = pygame.Rect(midpoint(center, self.rect.bottomleft), (50, 50))
			# self.rrect = pygame.Rect(midpoint(center, self.rect.topleft), (50, 50))
			self.lrect=pygame.Rect(midpoint_2(center, self.rect.midbottom), (100, 50))
			self.rrect=pygame.Rect(midpoint_2(center, self.rect.midtop), (100, 50))
			self.vision=pygame.Rect(self.rect.topleft, (75, 100))

	def rotateright(self):
		self.angle -= angle_diff*delta
		self.angle %= 360

	def rotateleft(self):
		self.angle += angle_diff*delta
		self.angle %= 360

	def ruleone(self):
		# boids steer away from other boids
		collidecheck=self.vision.collidelistall([i for i in recs if i != self.image_rect])
		if collidecheck != []:
			for i in collidecheck:
				if self.rrect.collidepoint(recs[i].center):
					self.angle += angle_diff*delta*bavoid
					self.angle %= 360
				if self.lrect.collidepoint(recs[i].center):
					self.angle -= angle_diff*delta*bavoid
					self.angle %= 360
				# return
			# for i in [random.choice(collidecheck)]:
			# 	if self.rrect.collidepoint(recs[i].center):
			# 		self.angle += angle_diff*delta*bavoid
			# 		self.angle %= 360
			# 	if self.lrect.collidepoint(recs[i].center):
			# 		self.angle -= angle_diff*delta*bavoid
			# 		self.angle %= 360
			# 	return
			
		else:
			self.color1=(255, 0, 0)
			self.color2=(255, 0, 0)

	def mousefollow(self):
		# boids steer towards the mouse pos
		center_angle= int(math.degrees(math.atan2(my - self.y, mx - self.x)))
		center_angle %= 360

		# if center_angle == int(self.angle): #dos not work
		# 	print('yey',int(self.angle), center_angle) #wrong
		# 	pygame.draw.line(screen, (200, 0, 0, 0), (self.x, self.y), (mx, my))
		# 	return

		if center_angle < self.angle:
			self.angle -= angle_diff*delta
			self.angle %= 360

		if center_angle > self.angle:
			self.angle += angle_diff*delta
			self.angle %= 360
		
		print(int(self.angle), center_angle)
		
		pygame.draw.line(screen, (200, 0, 0, 0), (self.x, self.y), (mx, my))


	def ruletwo(self):
		# boids steer in direction of nearby boids
		angles=[ready[i].angle for i in self.vision.collidelistall([i.image_rect for i in ready if i != self])]
		if angles != []:
			avg_angle=sum(angles)/len(angles)
			if avg_angle < self.angle:
				self.angle -= angle_diff*delta*bfollow
				self.angle %= 360
			elif avg_angle > self.angle:
				self.angle += angle_diff*delta*bfollow
				self.angle %= 360

	def rulethree(self):
		# boids steer towrards center if other boids
		points=[recs[i].center for i in self.vision.collidelistall([i for i in recs if i != self.image_rect])]
		if points != []:
			point_x, point_y=avgpoint([i[0] for i in points], [i[1] for i in points], len(points))
			center_angle=math.degrees(math.atan2(point_y - self.y, point_x - self.x))
			if center_angle > self.angle:
				self.angle += angle_diff*delta*bcohes
				self.angle %= 360

			if center_angle < self.angle:
				self.angle -= angle_diff*delta*bcohes
				self.angle %= 360

	def rulefour(self):
		# boids steer away from the edges
		collidecheck = self.vision.collidelistall(walls)
		if collidecheck != []:
			self.dontskiprule123 == False
			for i in collidecheck:
				if self.left == False and self.right == False:
					if self.lrect.colliderect(walls[i]) and self.rrect.colliderect(walls[i]):
						if random.choice([0, 1]):
							self.right= True
						else:
							self.left = True
					elif self.rrect.colliderect(walls[i]):
						self.left = True
					elif self.lrect.colliderect(walls[i]):
						self.right = True

				if self.left:
					self.rotateleft()
					self.rotateleft()
					
				if self.right:
					self.rotateright()
					self.rotateright()

				self.angle %= 360
		else:
			self.dontskiprule123 == True
			self.right = False
			self.left = False

	def rulefive(self):
		# boids cannot intercept with other boids
		points = [recs[i].center for i in self.image_rect.collidelistall([i for i in recs if i != self.image_rect])]
		# if points != []:
		# 	ready.remove(self)
		# 	return
		if points != []:
			for i ,j in points:
				if self.x >= i:
					self.x += bs*delta
				else:
					self.x -= bs*delta
				if self.y >= j:
					self.y += bs*delta
				else:
					self.y -= bs*delta
	


	def setpos(self, diff):
		self.x += diff*(math.cos(math.radians(self.angle)))
		self.y -= diff*(math.sin(math.radians(self.angle)))

dx=(-30, 815)
dy=(-30, 615)

white=pygame.transform.scale(pygame.image.load('assets//paper-plane.png'), (25, 25))
# white.convert_alpha()



def move(i):
	global bs
	# player ship - arrow keys
	if player == i:
		i.updategame()
	else:
		i.updategame()
		i.setpos(-bs*delta)
		if i.dontskiprule123:
			# i.ruleone()
			# i.ruletwo()
			# i.rulethree()
			i.mousefollow()
			# i.rulefive()
		# i.rulefour()





# formatting configuration menu
def multlines(text, configs, fontsize):
	text=text.replace('True', 'ON').replace('False', 'OFF').splitlines()
	for i, j in enumerate(text):
		screen.blit(configs.render(j, True, (0, 0, 0)), (0, fontsize*i))
		screen.blit(configs.render(j, True, (0, 0, 0)), (0, fontsize*i))


def update():
	# drawing backround
	if pyupdate:
		screen.fill((255, 255, 255))
		# screen.fill((30, 20, 30))

	# drawsconfigs
	if configuration:
		multlines(text, configs, 12)
	# update player,enemy position
	for i in ready:
		move(i)

	# drawing border
	if drawrecs:
		for i in walls:
			pygame.draw.rect(screen, (255, 0, 0), i)

	# creates frame in window
	pygame.display.update()
	# updates root
	root.update()

configs=pygame.font.Font('freesansbold.ttf', 12)




walls = [pygame.Rect(0, -25, 800, 50), pygame.Rect(0, 575, 800, 50), pygame.Rect(-25, 0, 50, 600), pygame.Rect(775, 0, 50, 600)]
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
player = gameobject(image=white, angle=random.randint(0, 359), pcolor=(255, 0, 0))
# ready.append(player)

while run:
	# returns each event in keyboard
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run=False
			continue
	# updating mouse pos
	mx, my=pygame.mouse.get_pos()

	# updating recs
	recs=[i.image_rect for i in ready]

	# updating delta value and setting frame rate
	delta=clock.tick(60)/1000

	# updating color
	if count % 2 == 0:
		color=next(colors)
	count += 1

	# updating game configs
	text=f'[F7]drawrecs: {drawrecs}\n[F8]update: {pyupdate}\n[F9]configs: {configuration}\n[\]exit\nfps: {round(clock.get_fps(), 2)}\nliveboids: {len(ready)}\nmouse: {mx, my}'

	# controlling ships
	keys=pygame.key.get_pressed()

	# allows keypresses 1 - K12 to change game settings
	if configcheck:
		if keys[pygame.K_F7]:
			drawrecs=not drawrecs
			configcheck=False

		elif keys[pygame.K_F8]:
			pyupdate=not pyupdate
			configcheck=False

		elif keys[pygame.K_F9]:
			configuration=not configuration
			configcheck=False

		elif keys[pygame.K_BACKSLASH]:
			run=False
			continue

		elif keys[pygame.K_SPACE]:
			ready.append(gameobject(white, angle = random.randint(0, 359)))
			# ready.append(gameobject(white, angle = 0))
			configcheck = False

	if keys[pygame.K_UP]:
		player.setpos(-bs*delta)

	if keys[pygame.K_LEFT]:
		player.rotateleft()

	if keys[pygame.K_RIGHT]:
		player.rotateright()

	if keys[pygame.K_DOWN]:
		player.setpos(bs*delta)

	# activate on release
	if event.type == pygame.KEYUP:
		if event.key == pygame.K_LSHIFT:
			ppress=True
			configcheck=True
		elif configcheck == False and event.key in [pygame.K_F7, pygame.K_F8, pygame.K_F9, pygame.K_BACKSLASH, pygame.K_SPACE]:
			configcheck=True

	update()
