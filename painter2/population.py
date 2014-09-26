from imagetools import ImageTools 
from dna import Dna
from random import triangular

class Population:
	def __init__(self, size, targetImage):
		self.size = size
		self.targetImage = targetImage
		self.artists = [Dna(size, 5) for i in xrange(size)]

	def luckyIndex(self):
		return int(triangular(0, self.size-1, 0)) 	# bias towards better fitness

	def evolve(self):
		self.newArtists = self.artists[:2] 			# top two always make it
		while len(self.newArtists) < self.size:
			child = self.artists[self.luckyIndex()].splice(self.artists[self.luckyIndex()])
			child.mutate()
			self.newArtists.append(child)
		self.artists = self.newArtists
		self.artists.sort(key=lambda dna: self.calcFitness(dna))
		
	def calcFitness(self, dna):
		image = ImageTools.imageFromDna(dna)
		fitness = ImageTools.compare(image, self.targetImage)
		return fitness
		

