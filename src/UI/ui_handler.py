from ..game_engine.state_manager import StateManager
from .slider import Slider


class UiHandler:

	def __init__(self) -> None:
		self.mass_slider = Slider(x=100, y=50, width=200, min_val=1, max_val=100, start_val=50, value_text='Mass')
		self.force_slider = Slider(x=400, y=50, width=600, min_val=1000, max_val=100000, start_val=50000, value_text='Force')
		

	def handle_events(self, events) -> None:
		self.mass_slider.handle_event(events)
		StateManager.set_mass(self.mass_slider.get_value())

		self.force_slider.handle_event(events)
		StateManager.set_force(self.force_slider.get_value())
		

	def draw(self, screen) -> None:
		self.mass_slider.draw(screen)
		self.force_slider.draw(screen)