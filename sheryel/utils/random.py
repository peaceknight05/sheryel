from .sequence import RANDOM, RANDOM_SEQUENCE_MAIN

def random_generator():
	"""Generator for random digits
	"""

	i, j = 0, 0
	while True:
		if j == len(RANDOM[RANDOM_SEQUENCE_MAIN[i]]):
			j = 0
			i += 1
		if i == len(RANDOM_SEQUENCE_MAIN):
			i = 0
		yield RANDOM[RANDOM_SEQUENCE_MAIN[i]][j]
		j += 1

g = random_generator()

def random():
	"""Returns a random digit from 0-9
	"""

	return next(g)

def randint(low, high):
	"""Returns a random number in the range [low, high] Number of digits must be between 1 and 10 and low and high must be at least 1 apart
	"""

	if len(str(low)) < 1 or len(str(high)) > 10 or low < 0 or low >= high:
		return -1

	num = -1
	while not low <= num and num <= high:
		num = random()
		if len(str(high)) == 1:
			break
		n = random() + 1
		while not len(str(low)) <= n and n <= len(str(high)):
			n = random() + 1
		for _ in range(n-1):
			num = num * 10 + random()

	return num

def shuffle(arr):
	"""Function that returns a shuffled array
	"""

	i = []
	for _ in range(len(arr)):
		n = randint(0, len(arr)-1)
		while n in i:
			remaining = list(set(list(range(len(arr)))).difference(i))
			if len(remaining) == 1:
				n = remaining[0]
				break
			n = randint(min(remaining), max(remaining))
			print(n)
		i.append(n)
		print()
	return [arr[j] for j in i]