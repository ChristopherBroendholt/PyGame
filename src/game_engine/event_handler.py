import pygame
from pygame.math import Vector2

from .state_manager import StateManager
from ..entities.ball import Ball


class EventHandler:

	def __init__(self, entity_manager) -> None:

		self.entity_manager = entity_manager
		

	def handle_events(self, events) -> bool:
		running = True

		for event in events:
			
			if event.type == pygame.QUIT:
				print('QUIT')
				running = False
				break

			if event.type == pygame.KEYDOWN:
				#Add a new ball
				if event.key == pygame.K_q:
					self.entity_manager.add(
						Ball(StateManager.get_mass())
					)

				# Delete all balls
				if event.key == pygame.K_e:
					self.entity_manager.delete_all()

				# Move all balls
				if event.key == pygame.K_a:
					self.entity_manager.apply_force(
						Vector2(
							-StateManager.get_force(),
							-StateManager.get_force()
						)
					)

				if event.key == pygame.K_d:
					self.entity_manager.apply_force(
						Vector2(
							StateManager.get_force(),
							-StateManager.get_force()
						)
					)

				if event.key == pygame.K_w:
					self.entity_manager.apply_force(
						Vector2(
							0,
							-StateManager.get_force()
						)
					)

			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 1:
					self.mouse_pos = Vector2(event.pos)


		return running
