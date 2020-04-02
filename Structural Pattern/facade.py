class Account:
	def __init__(self) -> None:
		self.account_no = 123456789
		
	def get_account_number(self) -> int:
		return self.account_no
		
		
class Fund:
	def __init__(self)-> None:
		self.balance = 1000
		
	def get_balance(self)-> float:
		return self.balance
		
	def decrease_cash(self, amount)-> None:
		self.balance -= amount
		
	def increase_cash(self, amount)-> None:
		self.balance += amount
		
	def make_deposit(self, amount)-> None:
		self.increase_cash(amount)

	
class Investment:
	def add_invest(self, amount, to)-> None:
		print(amount, " to ", to)
	
	
class BankServiceFacade:

	def __init__(self)-> None:
		self.invest = Investment()
		self.fund = Fund()
		self.account = Account()

		
	def get_account_number(self)-> int:
		self.account_number = self.account.get_account_number()
		return self.account_number


	def withdrawCash(self, amount)-> float:
		self.fund.decrease_cash(amount)
		return self.fund.get_balance()

acc = BankServiceFacade()
print(acc.withdrawCash(1))
