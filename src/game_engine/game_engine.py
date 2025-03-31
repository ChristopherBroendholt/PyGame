import sys
import pygame
from pygame.math import Vector2

from ..UI.ui_handler import UiHandler

from ..world.world_builder import WorldBuilder

from .event_handler import EventHandler
from .entity_manager import EntityManager


class GameEngine:



	def __init__(self) -> None:

		pygame.init()
		pygame.display.set_caption('Cygni Demo')
		pygame.font.init()

		self.screen = pygame.display.set_mode((1200, 800))
		self.clock = pygame.time.Clock()
		
		self.running = False

		self.world_builder = WorldBuilder()
		
		self.ui_handler = UiHandler()
		self.entity_manager = EntityManager()
		self.event_handler = EventHandler(self.entity_manager)


	def run(self) -> None:
		self.running = True

		while self.running:
			self.game_loop()

		pygame.quit()
		sys.exit()


	def game_loop(self) -> None:
		self.delta_time = self.clock.tick(300) / 1000.0

		
		self.handle_events()
		self.render()


	def handle_events(self) -> None:

		events = pygame.event.get()

		self.running = self.event_handler.handle_events(events)
		self.ui_handler.handle_events(events)


	def render(self) -> None:

		self.screen.fill((30, 30, 30))
		self.ui_handler.draw(self.screen)
		self.world_builder.draw(self.screen)
		
		self.entity_manager.draw(self.screen, self.delta_time)

		pygame.display.flip()
