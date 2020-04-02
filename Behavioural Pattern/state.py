from abc import ABC, abstractmethod
from math import floor


class State(ABC):

    @abstractmethod
    def insertDollar(self) -> None:
        pass

    @abstractmethod
    def ejectMoney(self) -> None:
        pass

    @abstractmethod
    def dispense(self) -> None:
        pass

class VendingMachine(ABC):

    @abstractmethod
    def setState(self) -> None:
        pass
        
    @abstractmethod 
    def getCount(self) -> int:
        pass
		
    @abstractmethod
    def insertDollar(self) -> None:
        pass

    @abstractmethod
    def ejectMoney(self) -> None:
        pass

    @abstractmethod
    def dispense(self) -> None:
        pass
        
    @abstractmethod
    def getOutOfStockState(self) -> State:
        pass
        
    @abstractmethod
    def getHasOneDollarState(self) -> State:
        pass
        
    @abstractmethod
    def getIdleState(self) -> State:
        pass

    @abstractmethod
    def doReleaseProduct(self) -> State:
        pass



class IdleState(State):

    def insertDollar(self, vm: VendingMachine) -> None:
        print("dollar inserted")
        vm.setState(vm.getHasOneDollarState())
        

    def ejectMoney(self, vm: VendingMachine) -> None:
        print("no money to return")
        
    def dispense(self, vm: VendingMachine) -> None:
        print("payment required")



class HasOneDollarState(State):

    def insertDollar(self, vm: VendingMachine) -> None:
        print("already have one dollar")
        

    def ejectMoney(self, vm: VendingMachine) -> None:
        print("returning money")
        vm.doReturnMoney()
        vm.setState(vm.getIdleState())
        
    def dispense(self, vm: VendingMachine) -> None:
        print("releasing product")
        if vm.getCount() > 1:
        	vm.doReleaseProduct()
        	vm.setState(vm.getIdleState())
        else:
        	vm.doReleaseProduct()
        	vm.setState(vm.getOutOfStockState())


class OutOfStockState(State):

    def insertDollar(self, vm: VendingMachine) -> None:
        print("Out Of Stock")
        vm.doReturnMoney()
        
    def ejectMoney(self, vm: VendingMachine) -> None:
        print("no money to return")
        
    def dispense(self, vm: VendingMachine) -> None:
        print("Out Of Stock")



class PopMachine(VendingMachine):

	def __init__(self, count) -> None:
		self.idleState = IdleState()
		self.hasOneDollarState = HasOneDollarState()
		self.outOfStockState = OutOfStockState()
		self.count = count
		
		if self.count > 0:
			self.currentState = self.idleState
		else:
			self.currentState = self.outOfStockState
			
	def getCount(self) -> int:
		return self.count
		
	def insertDollar(self) -> None:
		self.currentState.insertDollar(self)
	
	def ejectMoney(self) -> None:
		self.currentState.ejectMoney(self)
        
	def dispense(self) -> None:
		self.currentState.dispense(self)

	def getOutOfStockState(self) -> State:
		return self.outOfStockState
        
	def getHasOneDollarState(self) -> State:
		return self.hasOneDollarState
        
	def getIdleState(self) -> State:
		return self.idleState

	def doReleaseProduct(self) -> State:
		self.count -= 1
        
	def setState(self, state: State) -> None:
		self.currentState = state
		print("Current State => ", self.currentState.__class__.__name__)
	
	def doReturnMoney(self):
		print("here is your Dollar Back")

vm = PopMachine(2)
vm.insertDollar()
vm.dispense()
vm.insertDollar()
vm.ejectMoney()


