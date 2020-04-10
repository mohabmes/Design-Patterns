from abc import ABC, abstractmethod

class Observer(ABC):

    @abstractmethod
    def update()-> None:
    	pass



class Subject(ABC):

    def __init__(self):
    	self.observers = []
    	
    	
    def registerObserver(self, observer : Observer) -> None:
    	self.observers.append(observer)
    	print(id(observer), ": Subscribed")


    def unregisterObserver(self, observer : Observer) -> None:
    	self.observers.remove(observer)
    	print(id(observer), ": Unsubscribed")
    
    
    def notify(self):
    	for observer in self.observers:
    		observer.update()



class Subscriber(Observer):

    def update(self) -> None:
    	print(id(self), ": New post notification")


class Blog(Subject):

    def getSubscriberCount(self) -> int:
    	return len(self.observers)
    	
    def newPost(self) -> None:
    	print("create new post .. ")
    	self.notify()





sub1 = Subscriber()
sub2 = Subscriber()

blog = Blog()
blog.registerObserver(sub1)
blog.registerObserver(sub2)

print(blog.getSubscriberCount())

blog.newPost()
blog.unregisterObserver(sub2)
print(blog.getSubscriberCount())

