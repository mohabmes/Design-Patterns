from abc import ABC, abstractmethod

class IComponent(ABC):
	@abstractmethod
	def play(self) -> None:
		pass
		
	@abstractmethod
	def setPlaySpeed(self, speed) -> None:
		pass
		
	@abstractmethod
	def getName(self) -> str:
		pass


class Playlist(IComponent):
	def __init__(self, playListName:str) -> None:
		self.playListName = playListName
		self.playlist = []
	
	def add(self, component:IComponent) -> None:
		self.playlist.append(component)
	
	def remove(self, component:IComponent) -> None:
		self.playlist.remove(component)
	
	def play(self) -> None:
		for component in self.playlist:
			component.play()

	def setPlaySpeed(self, speed:int) -> None:
		for component in self.playlist:
			component.setPlaySpeed(speed)

	def getName(self) -> str:
		return self.playListName


class Song(IComponent):
	def __init__(self, songName:str, artist:str, speed:int=1) -> None:
		self.songName = songName
		self.artist = artist
		self.speed = speed
		
	def play(self) -> None:
		print("Playing | {} - {}".format(self.songName,self.artist))

	def setPlaySpeed(self, speed:int) -> None:
		self.speed = speed

	def getName(self) -> str:
		return self.playListName


playlist_1 = Playlist("My Famous songs")
playlist_2 = Playlist("All my songs")

song_1 = Song("Bla bla bla", "Mohab")
song_2 = Song("Yada yada yada", "Mohab")
playlist_1.add(song_1)
playlist_1.add(song_2)

song_3 = Song("Hamda", "Mohab")
playlist_2.add(song_3)
playlist_2.add(playlist_1)

playlist_2.play()
