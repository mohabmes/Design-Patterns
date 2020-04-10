from abc import ABC, abstractmethod

class Command(ABC):

    @abstractmethod
    def execute()-> None:
    	pass
    
    @abstractmethod
    def unexecute()-> None:
    	pass



class Document():

    def __init__(self):
    	self.text = ""
    	
    	
    def getText(self):
    	return self.text


    def insertText(self, position, newtext):
    	orginal = self.text
    	self.text = orginal[ : position] + newtext + orginal[position : ]
    
    
    def deleteText(self, position, textLength):
    	orginal = self.text
    	self.text = orginal[ : position] + orginal[position+textLength : ]



class PasteCommand(Command):

    def __init__(self, document:Document, position:int, text:str):
    	self.document = document
    	self.text = text
    	self.position = position
    
    def execute(self):
    	self.document.insertText(self.position, self.text)
    
    
    def unexecute(self):
    	self.document.deleteText(self.position, len(self.text))



class Editor():

    def invokePasteCommand(self, command:Command):
    	command.execute()

    def invokeUndoPasteCommand(self, command:Command):
    	command.unexecute()


editor = Editor()
doc = Document()
doc.text = "the original text goes here"
pasteCommand = PasteCommand(doc, 0, "Hello World!")
editor.invokePasteCommand(pasteCommand)
print(doc.getText())
editor.invokeUndoPasteCommand(pasteCommand)
print(doc.getText())


