
from src.controllers.base_controller import BaseController

class CommandRouter():
    def __init__(self, controllers: list[BaseController]):
        self.controlelers = controllers
    
    def dispatch(self, command):
        for controller in self.controlelers:
            if controller.can_handel(command=command):
                controller.execute(command=command)
                return True
            return False