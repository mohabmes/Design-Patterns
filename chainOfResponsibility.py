from abc import ABC, abstractmethod
from math import floor

class Handler(ABC):

    @abstractmethod
    def set_next(self):
        pass

    @abstractmethod
    def handle(self):
        pass


class AbstractHandler(Handler):

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: str) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class Dispenser10(AbstractHandler):
    def handle(self, request: int) -> str:
        dispensingCnt = 0
        if request >= 10:
                dispensingCnt = floor(request/10)
                print("Dispenser10 : {} £10 note".format(dispensingCnt))
                
        remaining = request - (10*dispensingCnt)
        if remaining > 0:
                print("Dispenser10 : Hey, I can't handle £{}".format(remaining))
                return super().handle(remaining)   


class Dispenser5(AbstractHandler):
    def handle(self, request: int) -> str:
        dispensingCnt = 0
        if request >= 5:
                dispensingCnt = floor(request/5)
                print("Dispenser20 : {} £5 note".format(dispensingCnt))
                
        remaining = request - (5*dispensingCnt)
        if remaining > 0:
                print("Dispenser20 : Hey, I can't handle £{}".format(remaining)) 
		

disp10 = Dispenser10()
disp10.set_next(Dispenser5())

disp10.handle(15)

