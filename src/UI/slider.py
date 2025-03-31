import pygame

class Slider:
	def __init__(self, x: int, y: int, width: int, min_val: int, max_val: int, start_val: int, value_text: str):
		self.x = x
		self.y = y
		self.width = width
		self.height = 6

		self.min_val = min_val
		self.max_val = max_val
		self.value = start_val

		self.thumb_radius = 10
		self.dragging = False

		self.value_text = value_text

	def handle_event(self, events):
		
		for event in events:
			if event.type == pygame.MOUSEBUTTONDOWN:
				if self._thumb_rect().collidepoint(event.pos):
					self.dragging = True

			elif event.type == pygame.MOUSEBUTTONUP:
				self.dragging = False

			elif event.type == pygame.MOUSEMOTION and self.dragging:
				self._update_value(event.pos[0])

	def _update_value(self, mouse_x: int):
		rel_x = max(self.x, min(mouse_x, self.x + self.width))
		percent = (rel_x - self.x) / self.width
		self.value = self.min_val + percent * (self.max_val - self.min_val)

	def _thumb_rect(self):
		thumb_x = self.x + (self.value - self.min_val) / (self.max_val - self.min_val) * self.width
		return pygame.Rect(thumb_x - self.thumb_radius, self.y - self.thumb_radius, self.thumb_radius * 2, self.thumb_radius * 2)

	def draw(self, screen):
		pygame.draw.rect(screen, (200, 200, 200), (self.x, self.y, self.width, self.height))
		
		thumb_x = self.x + (self.value - self.min_val) / (self.max_val - self.min_val) * self.width
		pygame.draw.circle(screen, (255, 100, 100), (int(thumb_x), self.y + self.height // 2), self.thumb_radius)

		font = pygame.font.SysFont("Arial", bold=True, size=16)
		text_surface = font.render(f'{self.value_text}: {round(self.value, 0)}', True, (255, 255, 255))
		
		screen.blit(text_surface, pygame.Vector2(self.x + self.width + 20, self.y - 6))

	def get_value(self):
		return self.value
