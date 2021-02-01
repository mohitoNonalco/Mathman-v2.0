import pygame
from pygame.locals import *
import random
import config
from config import *
import colors
from colors import *

class Block(pygame.sprite.Sprite):
	def __init__(self, img, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(img)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y

class Player(Block):
	def __init__(self, img, x, y):
		Block.__init__(self, img, x, y)
		self.image = pygame.image.load(img)
		self.rect = self.image.get_rect()
		self.rect.bottom = 480
		self.rect.left = 0
		self.speed_x = 5
		self.speed_y = 0
		self.speed = 8
		self.jump = 13
		self.jump_count = 0
		self.gravity = GRAVITY
		self.win = 0
		self.lose = True
		self.number = ""
		self.questions = str(random.randint(0, 10)) + " + " + str(random.randint(0, 10))
		self.record = 0
		print(self.questions)
		self.texte = self.questions
		self.questionright = False
		self.f2 = pygame.font.SysFont('comic sans ms', 70)


	def collide_y(self, events, hard_blocks):
		self.rect.y += self.speed_y
		for block in hard_blocks:
			if pygame.sprite.collide_rect(self, block):
				if self.speed_y > 0:
					self.rect.bottom = block.rect.top
					self.jump_count = 2
					self.speed_y = 0
				if self.speed_y < 0:
					self.rect.top = block.rect.bottom
					self.speed_y = 0

	def collide_x(self, events, hard_blocks):
		self.rect.x += self.speed_x
		for block in hard_blocks:
			if pygame.sprite.collide_rect(self, block):
		
				if self.speed_x > 0:
					self.rect.right = block.rect.left
					
				if self.speed_x < 0:
					self.rect.left = block.rect.right

	def slime_check(self, hard_blocks, slime):
		for block in slime:
			if self.speed_y > 0:
				if pygame.sprite.collide_rect(self, block):
					self.speed_y = 20
					block.kill()
					self.jump_count = 1
					

	def space_check(self, hard_blocks, space):
		for block in space:
			if pygame.sprite.collide_rect(self, block):
				self.lose = True
				self.menu_running = True

	def number_check(self, numberadd):
		self.number += numberadd
		print(self.number)
		if str(self.number) == str(eval(self.questions)):
			self.number = ""
			self.speed_y = -20
			self.record += 1
			print('Вы решили', self.record, 'примеров')
			if self.record < 10:
				self.questions = str(random.randint(0, 10)) + " + " + str(random.randint(0, 10))
			elif self.record > 20:
				self.questions = str(random.randint(0, 10)) + " * " + str(random.randint(0, 10))
			else:
				self.questions = str(random.randint(0, 100)) + " + " + str(random.randint(0, 100))

			print(self.questions)
			self.texte = self.questions
			print()
		if len(self.number) >= len(str(eval(self.questions))):
			self.number = ""
			print(self.questions)
			self.texte = self.questions

			



	def update(self, events, hard_blocks, slime, space):

		if self.rect.bottom >= WIN_HEIGHT:
			self.lose = True
			self.menu_running = True

		if self.speed_y > 14:
			self.speed_y = 14

		if self.rect.bottom <= 0:
			self.rect.bottom = 0
		
		if self.rect.left <= 0:
			self.rect.left = 0
		if self.rect.right >= WIN_WIDTH:
			self.win = 1
			self.rect.x = 0



		keys = pygame.key.get_pressed()

		for event in events:
			if event.type == KEYDOWN:
				if event.key == K_1:
					self.number_check("1")
				if event.key == K_2:
					self.number_check("2")
				if event.key == K_3:
					self.number_check("3")
				if event.key == K_4:
					self.number_check("4")
				if event.key == K_5:
					self.number_check("5")
				if event.key == K_6:
					self.number_check("6")
				if event.key == K_7:
					self.number_check("7")
				if event.key == K_8:
					self.number_check("8")
				if event.key == K_9:
					self.number_check("9")
				if event.key == K_0:
					self.number_check("0")



				


		self.speed_y = self.speed_y + self.gravity

		self.collide_y(events, hard_blocks)
		self.collide_x(events, hard_blocks)
		self.slime_check(hard_blocks, slime)
		self.space_check(hard_blocks, space)

	

class Game:
	def __init__(self):
		pygame.init()
		self.win_size = (WIN_WIDTH, WIN_HEIGHT)
		self.window = pygame.display.set_mode(self.win_size)
		self.running = True
		self.menu_running = True
		self.clock = pygame.time.Clock()
		self.bg_color = BG_COLOR
		self.background = pygame.Surface(self.win_size)
		self.background.fill(self.bg_color)
		self.entities = pygame.sprite.Group()
		self.hard_blocks = pygame.sprite.Group()
		self.slime = pygame.sprite.Group()
		self.space = pygame.sprite.Group()
		self.menu_image = pygame.image.load('images\\menu_screen.png')
		self.current = 0
		self.move = 0


	def menu_events(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				self.running = False
				self.menu_running = False
			if event.type == KEYDOWN:
				self.menu_running = False
				self.player.lose = False


	def menu_update(self):
		pygame.display.set_caption('Mathman')
		self.clock.tick(FPS)


	def menu_render(self):
		if self.player.lose == True:
			self.window.blit(self.menu_image, (0, 0))
			pygame.display.flip()                


	def menu_run(self):
		while self.menu_running == True:
			self.menu_events()
			self.menu_update()
			self.menu_render()


	def game_run(self):
		self.load_map('map1.txt')
		while self.running == True:
			self.text2 = self.player.f2.render(self.player.texte, False, (218, 105, 78))
			self.text3 = self.player.f2.render(self.player.number, False, (218, 105, 78))
			self.events()
			self.update()
			self.render()

			
			if self.player.win == 1:
				self.player.win = 0
				while self.current == self.move:
					self.move = random.choice(range(10))
				if self.current < self.move:
					for i in range(self.move - self.current):
						for block in self.entities:
							block.rect.x -= WIN_WIDTH
				else:
					for i in range(self.current - self.move):
						for block in self.entities:
							block.rect.x += WIN_WIDTH
				self.current = self.move

			if self.player.lose == True:
				for entity in self.entities:
					entity.kill()
				self.load_map('map1.txt')
				self.menu_running = True
				self.menu_run()


	def events(self):
		event_list = pygame.event.get()
		self.player.update(event_list, self.hard_blocks, self.slime, self.space)
		for event in event_list:
			if event.type == QUIT:
				self.running = False
			if event.type == KEYUP:
				if event.key == K_ESCAPE:
					self.running = False



	def update(self):
		self.clock.tick(FPS)
		pygame.display.set_caption('Mathman, Рекорд: ' + str(self.player.record))
		# print(self.player.rect.topleft)

	def render(self):
		self.window.blit(self.background, (0, 0))
		self.window.blit(self.text2, (570, 5))
		self.window.blit(self.text3, (570, 100))
		self.entities.draw(self.window)
		pygame.display.flip()                


	def load_map(self, path):
		self.player = Player(PLAYER, WIN_HEIGHT/2, WIN_WIDTH/2)
		self.entities.add(self.player)
		with open(path, 'r') as file:
			for y, line in enumerate(file):
				for x, letter in enumerate(line):
					if letter in MAP_KEYS.keys():
						if letter == 'p':
							self.player.rect.top = y * BLOCK_SIZE
							self.player.rect.left = x * BLOCK_SIZE
						else:
							block = Block(MAP_KEYS[letter], x * BLOCK_SIZE, y * BLOCK_SIZE)
							self.entities.add(block)
							if letter in HARD_BLOCKS:
								self.hard_blocks.add(block)
							if letter == 's':
								self.slime.add(block)
							if letter == 'r':
								self.space.add(block)
							





Game().game_run()