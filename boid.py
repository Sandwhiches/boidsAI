import pygame
import math
import random
import time
from itertools import cycle
from tkinter import *
root = Tk()
root.geometry('186x600')
root.geometry('+45+69')
root.title('configs')
bs = 100
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
	btext.set(f'R1W : {str(bavoid)}\nR2W : {str(bfollow)}\nR3W : {str(bcohes)}')

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
	# for i in range(5) : ready.append(gameobject(pygame.image.load(fish()), angle = random.randint(0, 359)))

def rem5():
	for i in range(5) : ready.pop()

def ruonec():
	global ruone_
	ruone_ = not ruone_
	ruone.set(f'RuleOne : {ruone_}')

def rutwoc():
	global rutwo_
	rutwo_ = not rutwo_
	rutwo.set(f'RuleTwo : {rutwo_}')

def ruthreec():
	global ruthree_
	ruthree_ = not ruthree_
	ruthree.set(f'RuleThree : {ruthree_}')

def rufourc():
	global rufour_
	rufour_ = not rufour_
	rufour.set(f'FollowMouse : {rufour_}')

def drawrecc():
	global drawrecs
	drawrecs = not drawrecs
	drawrec.set(f'DrawRecs : {drawrecs}')

def updatec():
	global pyupdate
	pyupdate = not pyupdate
	update.set(f'Update : {pyupdate}')

def avoidwallc():
	global avoidwall
	avoidwall = not avoidwall
	avoidwalls.set(f'AvoidWall : {avoidwall}')

def phasec():
	global phase
	phase = not phase
	phases.set(f'NotPhase : {phase}')

ruone_ = True
rutwo_ = True
ruthree_ = True
rufour_ = False
drawrecs = False
pyupdate = False
avoidwall = False
phase = False

text1.set(bs)
button = Button(root, text = 'Inc speed', command = incspd)
button.grid(row = 0, column = 0, sticky = W + E + N + S, ipady = 4)
button1 = Button(root, text='Dec speed', command = decspd)
button1.grid(row = 0, column= 1, sticky = W + E + N + S, ipady = 4)
textbox1 = Label(root, textvariable = text1, relief = GROOVE)
textbox1.grid(row = 0, column = 2, sticky = W + E + N + S, ipady = 4)

text2.set(angle_diff)
button3 = Button(root, text = 'Inc angle', command = incangle, bd = 2)
button3.grid(row = 1, column = 0, sticky = W + E + N + S, ipady = 4)
button4 = Button(root, text = 'Dec angle', command = decangle, bd = 2)
button4.grid(row = 1, column = 1, sticky = W + E + N + S, ipady = 4)
textbox3 = Label(root, textvariable = text2, relief = GROOVE)
textbox3.grid(row = 1, column = 2, sticky = W + E + N + S, ipady = 4)

btext = StringVar()
btext.set(f'R1W : {str(bavoid)}\nR2W : {str(bfollow)}\nR3W : {str(bcohes)}')
button2 = Button(root, text = 'Randomize Bias', command = rando_bias, anchor = W, bd = 2)
button2.grid(row = 2, column = 0, sticky = W + E + N + S, ipady = 4)
textbox2 = Label(root, textvariable = btext, relief = GROOVE)
textbox2.grid(row = 2, column = 1, columnspan = 3, sticky = W + E + N + S, ipady = 4)

button5 = Button(root, text = 'Add 5 boids', command = add5, bd = 2)
button5.grid(row = 3, column = 0, sticky = W + E + N + S, ipady = 4)

button6 = Button(root, text = 'Remove 5 boids', command = rem5, bd = 2)
button6.grid(row = 3, column = 1, columnspan = 2, sticky = W + E + N + S, ipady = 4)

ruone = StringVar()
ruone.set(f'RuleOne : {ruone_}')
button7 = Button(root, textvariable =ruone , command = ruonec, anchor = W, bd = 2)
button7.grid(row = 4, column = 0, columnspan = 3, sticky = W + E + N + S, ipady = 4)

rutwo = StringVar()
rutwo.set(f'RuleTwo : {rutwo_}')
button8 = Button(root, textvariable = rutwo, command = rutwoc, anchor = W, bd = 2)
button8.grid(row = 5, column = 0, columnspan = 3, sticky = W + E + N + S, ipady = 4)

ruthree = StringVar()
ruthree.set(f'RuleThree : {ruthree_}')
button9 = Button(root, textvariable = ruthree, command = ruthreec, anchor = W, bd = 2)
button9.grid(row = 6, column = 0, columnspan = 3, sticky = W + E + N + S, ipady = 4)

rufour = StringVar()
rufour.set(f'FollowMouse : {rufour_}')
button10 = Button(root, textvariable = rufour, command = rufourc, anchor = W, bd = 2)
button10.grid(row = 7, column = 0, columnspan = 3, sticky = W + E + N + S, ipady = 4)

avoidwalls = StringVar()
avoidwalls.set(f'AvoidWall : {avoidwall}')
button12 = Button(root, textvariable = avoidwalls, command = avoidwallc, anchor = W, bd = 2)
button12.grid(row = 8, column = 0, columnspan = 3, sticky = W + E + N + S, ipady = 4)

phases = StringVar()
phases.set(f'NotPhase : {phase}')
button14 = Button(root, textvariable = phases, command = phasec, anchor = W, bd = 2)
button14.grid(row = 9, column = 0, columnspan = 3, sticky = W + E + N + S, ipady = 4)

drawrec = StringVar()
drawrec.set(f'Drawrecs : {drawrecs}')
button11 = Button(root, textvariable = drawrec, command = drawrecc, anchor = W, bd = 2)
button11.grid(row = 10, column = 0, columnspan = 3, sticky = W + E + N + S, ipady = 4)

update = StringVar()
update.set(f'Update : {pyupdate}')
button12 = Button(root, textvariable = update, command = updatec, anchor = W, bd = 2)
button12.grid(row = 11, column = 0, columnspan = 3, sticky = W + E + N + S, ipady = 4)

fps = StringVar()
label1 = Label(root, textvariable = fps, anchor = W, relief = GROOVE)
label1.grid(row = 12, column = 0, columnspan = 3, sticky = W + E + N + S, ipady = 4)

mousepos = StringVar()
label2 = Label(root, textvariable = mousepos, anchor = W, relief = GROOVE)
label2.grid(row = 13, column = 0, columnspan = 3, sticky = W + E + N + S, ipady = 4)

liveboid = StringVar()
label3 = Label(root, textvariable = liveboid, anchor = W, relief = GROOVE)
label3.grid(row = 14, column = 0, columnspan = 3, sticky = W + E + N + S, ipady = 4)

testing = StringVar()
label4 = Label(root, textvariable = testing, anchor = W, relief = GROOVE)
label4.grid(row = 15, column = 0, columnspan = 3, sticky = W + E + N + S, ipady = 4)

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

# colors = cycle(((0, 255, 0), (10, 255, 0), (20, 255, 0), (30, 255, 0), (40, 255, 0), (50, 255, 0), (60, 255, 0), (70, 255, 0), (80, 255, 0), (90, 255, 0), (100, 255, 0), (110, 255, 0), (120, 255, 0), (130, 255, 0), (140, 255, 0), (150, 255, 0), (160, 255, 0), (170, 255, 0), (180, 255, 0), (190, 255, 0), (200, 255, 0), (210, 255, 
# 0), (220, 255, 0), (230, 255, 0), (240, 255, 0), (250, 255, 0), (255, 255, 0), (255, 245, 0), (255, 235, 0), (255, 225, 0), (255, 215, 0), (255, 205, 0), (255, 195, 0), (255, 185, 0), (255, 175, 0), (255, 165, 0), (255, 155, 0), (255, 145, 0), (255, 135, 0), (255, 125, 0), (255, 115, 0), (255, 105, 0), (255, 95, 0), (255, 85, 0), (255, 75, 0), (255, 65, 0), (255, 55, 0), (255, 45, 0), (255, 35, 0), (255, 25, 0), (255, 15, 0), (255, 5, 0), (255, 0, 0), (255, 0, 10), (255, 0, 20), (255, 0, 30), (255, 0, 40), (255, 0, 50), (255, 0, 60), (255, 0, 70), (255, 0, 80), (255, 0, 90), (255, 0, 100), (255, 0, 110), (255, 0, 120), (255, 0, 130), (255, 0, 140), (255, 0, 150), (255, 0, 160), (255, 0, 170), (255, 0, 180), (255, 0, 190), (255, 0, 200), (255, 0, 210), (255, 0, 220), (255, 0, 230), (255, 0, 240), (255, 0, 250), (255, 0, 255), (245, 0, 255), (235, 0, 255), (225, 0, 255), (215, 0, 255), (205, 0, 255), (195, 0, 255), (185, 0, 255), (175, 
# 0, 255), (165, 0, 255), (155, 0, 255), (145, 0, 255), (135, 0, 255), (125, 0, 255), (115, 0, 255), (105, 0, 255), (95, 0, 255), (85, 0, 255), (75, 0, 255), (65, 0, 255), (55, 0, 255), (45, 0, 255), (35, 0, 255), (25, 0, 255), (15, 0, 255), (5, 0, 255), (0, 0, 255), (0, 10, 255), (0, 20, 255), (0, 30, 255), (0, 40, 
# 255), (0, 50, 255), (0, 60, 255), (0, 70, 255), (0, 80, 255), (0, 90, 255), (0, 100, 255), (0, 110, 255), (0, 120, 255), (0, 130, 255), (0, 140, 255), (0, 150, 255), (0, 160, 255), (0, 170, 255), (0, 180, 255), (0, 190, 255), (0, 200, 255), (0, 210, 255), (0, 220, 255), (0, 230, 255), (0, 240, 255), (0, 250, 255)))

# colors = cycle(((65, 0, 255), (55, 0, 255), (45, 0, 255), (35, 0, 255), (25, 0, 255), (15, 0, 255), (5, 0, 255), (0, 0, 255), (0, 10, 255), (0, 20, 255), (0, 30, 255), (0, 40, 
# 255), (0, 50, 255), (0, 60, 255), (0, 70, 255), (0, 80, 255), (0, 90, 255), (0, 100, 255), (0, 110, 255), (0, 120, 255), (0, 130, 255), (0, 140, 255), (0, 150, 255), (0, 160, 255), (0, 170, 255), (0, 180, 255), (0, 190, 255), (0, 200, 255), (0, 210, 255), (0, 220, 255), (0, 230, 255), (0, 240, 255), (0, 250, 255)))

color=next(colors)

angles = list(range(360))




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
		self.original_image = pygame.transform.scale(image, size())
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

	def move_to_angle(self, target, bias):
		angle = int(self.angle)
		target = int(target)
		if target > angle:
			la = len(angles[angle:target + 1])
			lb = len(angles[:angle] + angles[target:])

			if la > lb:
				self.angle -= angle_diff*delta*bias
				self.angle %= 360
			elif la < lb:
				self.angle += angle_diff*delta*bias
				self.angle %= 360

		elif target < angle:
			la = len(angles[target:angle + 1])
			lb = len(angles[:target] + angles[angle:])

			if la < lb:
				self.angle -= angle_diff*delta*bias
				self.angle %= 360
			elif la > lb:
				self.angle += angle_diff*delta*bias
				self.angle %= 360

	def rotateright(self):
		self.angle -= angle_diff*delta
		self.angle %= 360

	def rotateleft(self):
		self.angle += angle_diff*delta
		self.angle %= 360

	def ruleone(self):
		if not ruone_:
			return
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
		else:
			self.color1=(255, 0, 0)
			self.color2=(255, 0, 0)

	def ruletwo(self):
		if not rutwo_:
			return
		# boids steer in direction of nearby boids
		angles=[ready[i].angle for i in self.vision.collidelistall([i.image_rect for i in ready if i != self])]
		if angles != []:
			avg_angle=sum(angles)/len(angles)
			self.move_to_angle(avg_angle, bfollow)

	def rulethree(self):
		if not ruthree_:
			return
		# boids steer towrards center if other boids
		points=[recs[i].center for i in self.vision.collidelistall([i for i in recs if i != self.image_rect])]
		if points != []:
			point_x, point_y = avgpoint([i[0] for i in points], [i[1] for i in points], len(points))
			center_angle = -math.degrees(math.atan2(point_y - self.y, point_x - self.x)) + 180
			self.move_to_angle(center_angle, bcohes)
			
	def mousefollow(self):
		if not rufour_:
			return
		# boids steer towards the mouse pos
		center_angle = -math.degrees(math.atan2(my - self.y, mx - self.x)) + 180
		self.move_to_angle(center_angle, 1)

		# pygame.draw.line(screen, (200, 0, 0, 0), (self.x, self.y), (mx, my))
		# testing.set(f'center_angle : {int(center_angle)}\nship_angle : {int(self.angle)}')

	def rulefour(self):
		if not avoidwall:
			return
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
		if not phase:
			return
		# boids cannot intercept with other boids
		points = [recs[i].center for i in self.image_rect.collidelistall([i for i in recs if i != self.image_rect])]
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

def size():
	s = random.randint(20, 45)
	w = random.randint(s - 5, s + 5)
	return (s, w)

# def fish():
# 	return random.choice(['assets//angelfish.png', 'assets//fish.png', 'assets//blue-tang-fish.png', 'assets//salmon.png', 'assets//shark.png', 'assets//tuna.png'])


white = pygame.image.load('assets//fish.png')
red = pygame.image.load('assets//fish.png')


def move(i):
	global bs
	# player ship - arrow keys
	if player == i:
		i.updategame()
	else:
		i.updategame()
		i.setpos(-bs*delta)
		if i.dontskiprule123:
			i.ruleone()
			i.ruletwo()
			i.rulethree()
			i.mousefollow()
			i.rulefive()
		i.rulefour()

def updatesc():
	# drawing backround
	if pyupdate:
		# screen.fill((0, 0, 0))
		screen.fill((255, 255, 255))
		# screen.fill(((190, 230, 250)))
		# screen.fill((30, 20, 30))
		# screen.fill((200, 230, 250))
		# screen.fill((r, g, b))
		

	# update player,enemy position
	for i in ready:
		move(i)

	# drawing border
	if drawrecs:
		for i in walls:
			pygame.draw.rect(screen, (200, 230, 250), i)

	# creates frame in window
	pygame.display.update()
	# updates root
	root.update()



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
player = gameobject(image=red, angle=random.randint(0, 359), pcolor=(255, 0, 0))
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

	fps.set(f'fps : {round(clock.get_fps(), 2)}')
	mousepos.set(f'mouse : {mx}, {my}')
	liveboid.set(f'liveboids : {len(ready)}')

	# controlling ships
	keys=pygame.key.get_pressed()

	if keys[pygame.K_UP]:
		player.setpos(-bs*delta)

	if keys[pygame.K_LEFT]:
		player.rotateleft()

	if keys[pygame.K_RIGHT]:
		player.rotateright()

	if keys[pygame.K_DOWN]:
		player.setpos(bs*delta)

	updatesc()
