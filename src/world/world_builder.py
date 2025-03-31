from dataclasses import dataclass
from typing import List
from pygame.math import Vector2
import pygame

@dataclass
class Line:
	start_pos: Vector2
	end_pos: Vector2


class WorldBuilder:
	
	horizontal_grid_lines: List[Line] = []
	vertical_grid_lines: List[Line] = []

	def __init__(self) -> None:
		self._initialyze_lines()

	
	def _initialyze_lines(self) -> None:	
		for x in range(100, 1150, 50):
			line = Line(
				start_pos=(x, 100),
				end_pos=(x, 700)
			)

			self.horizontal_grid_lines.append(line)

		for y in range(100, 750, 50):
			line = Line(
				start_pos=(100, y),
				end_pos=(1100, y)
			)

			self.vertical_grid_lines.append(line)


	def draw(self, screen) -> None:
		
		font = pygame.font.SysFont('Arial', bold=True, size=16)

		x = 0

		for line in self.horizontal_grid_lines: 
			pygame.draw.line(screen, (70, 70, 70), line.start_pos, line.end_pos, 2)

			text_surface = font.render(str(x), True, (255, 255, 255))
			screen.blit(text_surface, line.end_pos + Vector2(-2, 15))

			x += 1

		y = len(self.vertical_grid_lines) - 1

		for line in self.vertical_grid_lines: 
			pygame.draw.line(screen, (70, 70, 70), line.start_pos, line.end_pos, 2)

			text_surface = font.render(str(y), True, (255, 255, 255))
			screen.blit(text_surface, line.start_pos - Vector2(20, 10))

			y -= 1
