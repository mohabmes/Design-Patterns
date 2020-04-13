class CoffeeMachineInterface():
	def FirstSelection() -> None:
		pass
	def SecondSelection(self) -> None:
		pass

class OldCoffeeMachine:
	def FirstSelection(self) -> str: 
		return "First Selection"
	def SecondSelection(self) -> str: 
		return "Second Selection"


class CoffeeTouchscreenAdapter(CoffeeMachineInterface):
	def __init__(self, oldcm:OldCoffeeMachine) -> None:
		self.oldcm = oldcm
		
	def FirstSelection(self) -> str:
		return self.updateOldRequest(self.oldcm.FirstSelection())
		
	def SecondSelection(self) -> str:
		return self.updateOldRequest(self.oldcm.SecondSelection())
	
	def updateOldRequest(self, oldreq) -> str:
		return "Updated " + oldreq
		


oldcm = OldCoffeeMachine()
adapter = CoffeeTouchscreenAdapter(oldcm)
updateRequest = adapter.FirstSelection()
print(updateRequest)
