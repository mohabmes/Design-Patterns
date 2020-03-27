class Singleton:
	__unique_instance = None
	
	def __init__(self):
		if Singleton.__unique_instance:
			print('Already instantiated')
		
	@classmethod		
	def get_instance(cls):
		if Singleton.__unique_instance is None:
			print('Create new Object...')
			cls.__unique_instance = Singleton()
		return cls.__unique_instance
		
		
a = Singleton()
obj1 = a.get_instance()

b = Singleton()
obj2 = b.get_instance()


if id(obj1) == id(obj2):
	print("the Same Object")

