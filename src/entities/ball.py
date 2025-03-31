import uuid
import pygame
from pygame.math import Vector2
import random

class Ball:

	def __init__(self, mass: float) -> None:

		self.id = str(uuid.uuid4())
		
		self.color = (255 - (mass * 2.55), 0, 0)
		self.radius = 10

		self.position = Vector2(600, 400)
		self.velocity = Vector2(0, 0)
		self.acceleration = Vector2(0, 0)

		self.gravity = Vector2(0, 1000)
		
		self.mass = mass
		self.drag = 0.8
		self.springiness = 0.5
		

	def apply_force(self, force:Vector2) -> None:
		self.acceleration += force / self.mass
		

	def _update(self, delta_time) -> None:

		gravity = self.gravity * self.mass
		drag = -self.velocity * self.drag

		force = gravity + drag
		
		self.apply_force(force)

		self.velocity += self.acceleration * delta_time
		self.position += self.velocity * delta_time

		self.acceleration = Vector2(0, 0)

		self._bounce()

	 
	def _bounce(self) -> None:
		if self.position.x - self.radius < 100:
			self.position.x = self.radius + 100
			self.velocity.x *= -self.springiness
		
		if self.position.x + self.radius > 1100:
			self.position.x = 1100 - self.radius
			self.velocity.x *= -self.springiness
		
		if self.position.y + self.radius > 700:
			self.position.y = 700 - self.radius
			self.velocity.y *= -self.springiness

		if self.position.y - self.radius < 100:
			self.position.y = 100 + self.radius
			self.velocity.y *= -self.springiness

		
	def _get_pos_string(self) -> str:
		x =	round((self.position.x - 100) / 50, 2)
		y = round((self.position.y - 100) / 50, 2)

		return f'X:{x} Y:{y}'


	def draw(self, screen) -> None:
		pygame.draw.circle(screen, self.color, self.position, self.radius)
		
		coordinate = self._get_pos_string()

		font = pygame.font.SysFont("Arial", bold=True, size=16)
		text_surface = font.render(coordinate, True, (255, 255, 255))
		screen.blit(text_surface, Vector2(self.position.x - 35, self.position.y + 15))
