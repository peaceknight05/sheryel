from sheryel.generate import Sheryel

sheryel = Sheryel().generate()

def cli():
	"""Command line interface
	"""

	print(*[next(sheryel) for _ in range(25)])
	print(*[next(sheryel) for _ in range(25)])
	print(*[next(sheryel) for _ in range(25)])
	print(*[next(sheryel) for _ in range(25)])
	print(*[next(sheryel) for _ in range(25)])

	return 0