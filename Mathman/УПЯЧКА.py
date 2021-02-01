self.rect.right = block.rect.left
self.rect.left = block.rect.right
self.rect.bottom = block.rect.top
self.rect.top = block.rect.bottom

				side_collide = False
				if self.speed_x > 0 and self.rect.right == block.rect.left:
					self.speed_x = 0
					self.rect.right = block.rect.left
					side_collide = True

				if self.speed_x > 0 and self.rect.left > block.rect.right:
					self.speed_x = 0
					self.rect.left = block.rect.right
					side_collide = True

				elif self.rect.top < block.rect.bottom and side_collide == False:
					self.speed_y = 0
					self.rect.top = block.rect.bottom

				if self.rect.bottom > block.rect.top and side_collide == False:
					self.rect.bottom = block.rect.top
					self.speed_y = 0
					self.jump_count = 2

		for event in events:
			if event.type == KEYDOWN:
				if event.key == K_w or event.key == K_SPACE:
					if self.jump_count > 0:
						self.speed_y = -self.jump
						self.jump_count -= 1
				if event.key == K_a:
					self.speed_x -= self.speed
				if event.key == K_d:
					self.speed_x += self.speed
			if event.type == KEYUP:
				if event.key == K_w or event.key == K_SPACE:
					if self.speed_y < 0:
						self.speed_y = -5
				if event.key == K_a:
					self.speed_x = 0
				if event.key == K_d:			
					self.speed_x = 0
					
