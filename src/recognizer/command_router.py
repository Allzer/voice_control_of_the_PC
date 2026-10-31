
from src.controllers.base_controller import BaseController

class CommandRouter():
    def __init__(self, controllers: dict[BaseController]):
        self.controllelers = controllers
    
    def dispatch(self, command: str):
        #TODO сделать вычленение нужного
        controller = self.controllelers.get(command.split()[0])
        if controller is not None:
            if controller.can_handel(command=command):
                controller.execute(command=command)
                return True
            return False