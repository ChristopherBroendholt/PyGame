from pygame.math import Vector2

class StateManager:

	mass: float = 1
	force: float = 1


	@classmethod
	def get_mass(cls) -> float:
		return cls.mass
	
	@classmethod
	def set_mass(cls, mass: float) -> None:
		cls.mass = mass


	@classmethod
	def get_force(cls) -> float:
		return cls.force
	
	@classmethod
	def set_force(cls, force: float) -> None:
		cls.force = force * 100