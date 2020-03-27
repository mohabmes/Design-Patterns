from abc import ABC, abstractmethod

class WebPage():
	def display(self) -> None:
		pass


class BasicWebPage(WebPage):
	def __init__(self, html:str, js:str, css:str) -> None:
		self.html = html
		self.js = js
		self.css = css
		
	def display(self) -> None:
		# Render HTML & stylesheet + Run js files
		print("BasicWebPage: Basic Web Page")


class WebPageDecorator(WebPage):
	def __init__(self, webpage:WebPage) -> None:
		self.webpage = webpage
		
	def display(self) -> None:
		self.webpage.display()
	
		
class AuthorizationWebPage(WebPageDecorator):
	def __init__(self, decoratedwebpage:WebPage) -> None:
		super().__init__(decoratedwebpage)
	
	def authorization(self) -> None:
		print("AuthorizationWebPage: authorization")
	
	def display(self) -> None:
		super().display()
		self.authorization()


class AuthenticationWebPage(WebPageDecorator):
	def __init__(self, decoratedwebpage:WebPage) -> None:
		super().__init__(decoratedwebpage)
	
	def authentication(self) -> None:
		print("AuthenticationWebPage: authentication")
		
	def display(self) -> None:
		super().display()
		self.authentication()


mypage = BasicWebPage('html', 'css', 'js')
mypage_dec1 = AuthorizationWebPage(mypage)
mypage_dec2 = AuthenticationWebPage(mypage_dec1)
mypage_dec2.display()
