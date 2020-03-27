from abc import ABC, abstractmethod

class IOrder(ABC):
	@abstractmethod
	def order_request(self) -> None:
		pass
		


class Warehouse(IOrder):
	def __init__(self, stock:str) -> None:
		self.stock = stock
		
	def order_request(self) -> None:
		print("Warehouse: Order Request ... Done")
		
		
		
class OrderfulfillmentProxy(IOrder):
	def __init__(self, warehouses:Warehouse, amount:int) -> None:
		self.warehouses = warehouses
		self.amount = amount
		
	def check_request(self) -> bool:
		# Check stock availability
		print("OrderfulfillmentProxy: Availabile ... Done")
		return True
		
	def check_access(self) -> bool:
		print("OrderfulfillmentProxy: Access granted ... Done")
		return True
		
	def order_request(self) -> None:
		if self.check_access() and self.check_request():
			self.warehouses.order_request()


warehouse = Warehouse(100)
order_proxy = OrderfulfillmentProxy(warehouse, 50)
order_proxy.order_request()
