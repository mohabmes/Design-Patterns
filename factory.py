from abc import ABC, abstractmethod

class Knife(ABC): # Product
	@abstractmethod
	def get_name(self) -> str:
		pass
	
	@abstractmethod
	def test(self) -> None:
		pass
		
	def pack(self) -> None:
		print(self.get_name(), ": pack()")


class ChefKnife(Knife): # Concrete product
	def get_name(self) -> str:
		self.name = "Chef Knife"
		return self.name
		
	def test(self) -> None:
		print(self.get_name(), ": test()")

class BreadKnife(Knife):  # Concrete product
	def get_name(self) -> str:
		self.name = "Bread Knife"
		return self.name

	def test(self) -> None:
		print(self.get_name(), ": test()")


class KnifeFactory(ABC): # creator
	
	def make_product(self, product_name) -> Knife:
		product = None
		
		if product_name == 'BreadKnife':
			product = BreadKnife()
		elif product_name == 'ChefKnife':
			product = ChefKnife()
		else:
			return product
		
		
		return product


class KnifeStore(KnifeFactory): # Concrete creator
	
	def order_product(self, product_name) -> Knife:
		product = self.make_product(product_name)
		
		product.test()	
		product.pack()
		
		return product
		

product1 = KnifeStore().order_product('BreadKnife')
product2 = KnifeStore().order_product('ChefKnife')


