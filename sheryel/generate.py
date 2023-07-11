import os
from .utils.random import shuffle

class Sheryel():
	"""Helper class to generate sheryel words

	:param dataset: name of word dataset to use, defaults to 'swords'
	:type dataset: str, optional
	"""

	def __init__(self, dataset='swords'):
		"""Constructor method
		"""

		dirname = os.path.dirname(__file__)
		filename = os.path.join(dirname, f"words/{dataset}.txt")
		with open(filename) as f:
			self.words = f.read().splitlines()
			self.remaining = shuffle(self.words.copy())

	def generate(self):
		"""Generator for sheryel words
		"""

		while True:
			if not self.remaining:
				self.remaining = shuffle(self.words.copy())
			yield self.remaining.pop() + "yel"
